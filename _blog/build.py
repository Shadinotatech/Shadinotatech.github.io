#!/usr/bin/env python3
"""Build the shadinotatech.com blog.

Reads _blog/posts/*.md (front matter + Markdown) and writes:
  blog/<slug>/index.html, blog/<slug>/og.png, blog/index.html, blog/feed.xml,
  sitemap.xml, and the "From the blog" block on index.html.

Usage:  python3 _blog/build.py          (run from anywhere)
Needs:  pip install markdown pillow
"""
import datetime as dt
import html
import json
import math
import os
import re
import sys
from pathlib import Path

try:
    import markdown
except ImportError:
    sys.exit("pip install markdown  (needed by _blog/build.py)")

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "_blog" / "posts"
OUT = ROOT / "blog"
SITE = "https://shadinotatech.com"
PLAY = "https://play.google.com/store/apps/details?id=com.shadinota.smartid&referrer=utm_source%3Dblog%26utm_medium%3Darticle"
AUTHOR = "Md. Ruhul Amin"
AUTHOR_ROLE = "Founder of Shadinota Tech and developer of CardCraft – ID Card Maker"

STATIC_PAGES = [
    ("/", "weekly", "1.0"),
    ("/cardcraft/", "monthly", "0.9"),
    ("/blog/", "daily", "0.8"),
]

# ---------------------------------------------------------------- parsing

def parse(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        sys.exit(f"{path.name}: missing front matter")
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"')
    for req in ("title", "description", "slug", "date"):
        if not meta.get(req):
            sys.exit(f"{path.name}: front matter needs '{req}'")
    meta.setdefault("updated", meta["date"])
    meta.setdefault("category", "Guides")
    meta["keywords"] = [k.strip() for k in meta.get("keywords", "").split(",") if k.strip()]
    meta["body_md"] = m.group(2)
    meta["draft"] = meta.get("draft", "false").lower() == "true"
    return meta


def render_md(md_text):
    md = markdown.Markdown(
        extensions=["tables", "toc", "attr_list", "md_in_html", "fenced_code", "sane_lists"],
        extension_configs={"toc": {"permalink": False, "toc_depth": "2-2"}},
    )
    body = md.convert(md_text)
    toc = [(t["id"], t["name"]) for t in md.toc_tokens]
    return body, toc


def extract_faq(md_text):
    m = re.search(r"^##\s+(Frequently asked questions|FAQ)\s*$(.*?)(?=^##\s|\Z)", md_text, re.S | re.M | re.I)
    if not m:
        return []
    items = []
    for q, a in re.findall(r"^###\s+(.+?)\s*$\n(.*?)(?=^###\s|\Z)", m.group(2), re.S | re.M):
        a = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", a)
        a = re.sub(r"[*_`]", "", a).strip()
        a = re.sub(r"\s+", " ", a)
        if a:
            items.append((q.strip(), a))
    return items


def words(md_text):
    return len(re.findall(r"\w+", re.sub(r"<[^>]+>", " ", md_text)))


def fmt_date(d):
    return dt.date.fromisoformat(d).strftime("%-d %B %Y")

# ---------------------------------------------------------------- OG image

def make_og(title, category, dest):
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        return False
    fonts = ROOT / "_blog" / "fonts"
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), (9, 9, 11))
    d = ImageDraw.Draw(img)
    # soft glow
    glow = Image.new("RGB", (W, H), (9, 9, 11))
    gd = ImageDraw.Draw(glow)
    for r in range(420, 0, -6):
        a = int(26 * (1 - r / 420))
        gd.ellipse((W - 260 - r, -160 - r, W - 260 + r, -160 + r), fill=(9 + a // 3, 9 + a, 11 + a // 1))
    img = Image.blend(img, glow, 0.9)
    d = ImageDraw.Draw(img)
    bold = ImageFont.truetype(str(fonts / "Inter-Bold.otf"), 64)
    med = ImageFont.truetype(str(fonts / "Inter-Medium.otf"), 28)
    d.text((80, 80), category.upper(), font=med, fill=(79, 227, 193))
    # wrap title
    lines, line = [], ""
    for w in title.split():
        test = (line + " " + w).strip()
        if d.textlength(test, font=bold) > W - 160 and line:
            lines.append(line)
            line = w
        else:
            line = test
    lines.append(line)
    size = 64
    if len(lines) > 4:
        bold = ImageFont.truetype(str(fonts / "Inter-Bold.otf"), 52)
        size = 52
    y = 150
    for ln in lines[:5]:
        d.text((80, y), ln, font=bold, fill=(244, 244, 245))
        y += int(size * 1.18)
    logo = ROOT / "assets" / "logo-white.png"
    if logo.exists():
        L = Image.open(logo).convert("RGBA").resize((64, 64))
        img.paste(L, (80, H - 120), L)
    d.text((164, H - 104), "shadinotatech.com/blog", font=med, fill=(161, 161, 170))
    dest.parent.mkdir(parents=True, exist_ok=True)
    img.save(dest, optimize=True)
    return True

# ---------------------------------------------------------------- templates

CSS = """
:root{--bg:#09090b;--bg2:#0f0f12;--card:#131317;--line:rgba(255,255,255,.08);--line2:rgba(255,255,255,.14);--fg:#f4f4f5;--muted:#a1a1aa;--dim:#71717a;--acc:#4fe3c1;--acc2:#8b9cff}
*{box-sizing:border-box}html{scroll-behavior:smooth;overflow-x:clip}
body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.75 Inter,system-ui,-apple-system,"Segoe UI",sans-serif;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}img{max-width:100%;height:auto}
.wrap{max-width:1200px;margin:0 auto;padding:0 24px}
.h{font-family:Sora,Inter,sans-serif;letter-spacing:-.03em;line-height:1.15}
.bgfx{position:fixed;inset:0;z-index:-1;pointer-events:none;background:radial-gradient(800px 500px at 85% -10%,rgba(79,227,193,.10),transparent 60%),radial-gradient(700px 500px at -10% 30%,rgba(139,156,255,.07),transparent 60%),var(--bg)}
header.top{position:sticky;top:0;z-index:50;backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);background:rgba(9,9,11,.72);border-bottom:1px solid var(--line)}
nav.main{display:flex;align-items:center;justify-content:space-between;height:68px;gap:16px}
.brand{display:flex;align-items:center;gap:12px;font:700 18px Sora,sans-serif;letter-spacing:-.02em}.brand img{width:36px;height:36px}
.links{display:flex;gap:4px}.links a{padding:8px 14px;border-radius:999px;font-size:14.5px;color:var(--muted)}.links a:hover,.links a.on{color:var(--fg);background:rgba(255,255,255,.06)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:46px;padding:11px 20px;border-radius:14px;font-weight:600;font-size:15px;border:1px solid var(--line2);background:rgba(255,255,255,.03);transition:.2s;color:var(--fg)}
.btn:hover{transform:translateY(-2px);border-color:rgba(255,255,255,.3)}.btn.pri{background:var(--fg);color:#09090b;border-color:var(--fg)}
@media(max-width:720px){.links{display:none}}
/* article */
.crumbs{font-size:14px;color:var(--dim);margin:40px 0 18px}.crumbs a:hover{color:var(--fg)}
.post-head{max-width:820px}
.cat{display:inline-block;font-size:12.5px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--acc);margin-bottom:14px}
.post-head h1{font-size:clamp(32px,4.6vw,54px);margin:0 0 18px}
.lede{font-size:clamp(18px,1.6vw,20px);color:var(--muted);margin:0 0 22px}
.meta{display:flex;flex-wrap:wrap;gap:8px 18px;font-size:14px;color:var(--dim);padding-bottom:28px;border-bottom:1px solid var(--line)}
.layout{display:grid;grid-template-columns:minmax(0,720px) 260px;gap:64px;justify-content:space-between;padding:40px 0 40px}
.toc{position:sticky;top:96px;align-self:start;font-size:14px;border-left:1px solid var(--line);padding-left:18px}
.toc b{display:block;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--dim);margin-bottom:10px}
.toc a{display:block;color:var(--muted);padding:5px 0;line-height:1.4}.toc a:hover{color:var(--fg)}
.toc a.btn{display:flex;color:#09090b;padding:8px 14px}
.toc .side-cta{margin-top:26px;padding:18px;border:1px solid var(--line2);border-radius:16px;background:var(--card)}
.toc .side-cta p{margin:0 0 12px;color:var(--muted);font-size:13.5px;line-height:1.5}
@media(max-width:1000px){.layout{grid-template-columns:minmax(0,1fr)}.toc{display:none}}
.prose h2{font-family:Sora,Inter,sans-serif;letter-spacing:-.025em;font-size:clamp(25px,2.6vw,32px);line-height:1.2;margin:56px 0 16px;scroll-margin-top:90px}
.prose h3{font-family:Sora,Inter,sans-serif;font-size:21px;letter-spacing:-.02em;margin:34px 0 10px;scroll-margin-top:90px}
.prose p,.prose li{color:#d4d4d8}.prose strong{color:var(--fg)}
.prose a{color:var(--acc);text-decoration:underline;text-underline-offset:3px;text-decoration-thickness:1px}
.prose ul,.prose ol{padding-left:24px}.prose li{margin:6px 0}
.prose blockquote{margin:28px 0;padding:18px 22px;border:1px solid rgba(79,227,193,.25);background:rgba(79,227,193,.06);border-radius:16px}
.prose blockquote p{margin:0;color:var(--fg)}
.prose table{width:100%;border-collapse:collapse;margin:24px 0;font-size:15px;display:block;overflow-x:auto}
.prose th,.prose td{border-bottom:1px solid var(--line2);padding:11px 12px;text-align:left;vertical-align:top;white-space:nowrap}
.prose td{white-space:normal}.prose th{color:var(--fg);font-weight:600;background:rgba(255,255,255,.03)}
.prose code{font-size:.9em;background:rgba(255,255,255,.07);padding:2px 6px;border-radius:6px}
.prose figure{margin:32px 0}.prose figure img,.prose figure svg{display:block;width:100%;border-radius:18px;border:1px solid var(--line)}
.prose figcaption{font-size:14px;color:var(--dim);margin-top:10px;text-align:center}
.prose hr{border:0;border-top:1px solid var(--line);margin:48px 0}
.keytakeaways{border:1px solid var(--line2);background:var(--card);border-radius:20px;padding:22px 26px;margin:0 0 32px}
.keytakeaways b{display:block;font-family:Sora,sans-serif;margin-bottom:6px}
.keytakeaways>p:first-child{margin-top:0}
.keytakeaways ul{margin:0}
.cta{margin:48px 0;border:1px solid var(--line2);border-radius:24px;padding:30px;background:linear-gradient(135deg,#15151a,#0d0d10);display:grid;grid-template-columns:72px 1fr;gap:20px;align-items:center}
.cta img{width:72px;height:72px;border-radius:18px}
.cta h3{margin:0 0 6px!important;font-size:21px}.cta p{margin:0 0 16px!important;color:var(--muted)!important;font-size:15.5px}
@media(max-width:600px){.cta{grid-template-columns:1fr}}
.author{display:flex;gap:16px;align-items:center;border-top:1px solid var(--line);margin-top:48px;padding-top:28px;font-size:15px;color:var(--muted)}
.author img{width:52px;height:52px}.author b{color:var(--fg);display:block}
.related{border-top:1px solid var(--line);padding:56px 0 24px}
.related h2{font-size:28px;margin:0 0 24px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:20px}
.pcard{border:1px solid var(--line);border-radius:22px;overflow:hidden;background:var(--card);transition:border-color .25s,transform .25s;display:flex;flex-direction:column}
.pcard:hover{border-color:var(--line2);transform:translateY(-3px)}
.pcard img{aspect-ratio:1200/630;object-fit:cover;width:100%;display:block;border-bottom:1px solid var(--line)}
.pcard .pb{padding:20px 22px 24px;display:flex;flex-direction:column;gap:8px}
.pcard .c{font-size:12px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--acc)}
.pcard h3{margin:0;font-size:20px}.pcard p{margin:0;color:var(--muted);font-size:15px;line-height:1.6}
.pcard .d{font-size:13px;color:var(--dim)}
.bloghero{padding:72px 0 40px;max-width:760px}
.bloghero h1{font-size:clamp(40px,6vw,72px);margin:12px 0 16px}.bloghero p{color:var(--muted);font-size:19px;margin:0}
footer{border-top:1px solid var(--line);margin-top:80px;padding:32px 0 40px;font-size:14px;color:var(--dim)}
footer .wrap{display:flex;flex-wrap:wrap;gap:12px 24px;justify-content:space-between}footer a:hover{color:var(--fg)}
"""

def head(title, desc, canonical, og, extra_ld="", og_type="article"):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
<link rel="icon" href="/favicon.ico?v=2" sizes="any">
<link rel="apple-touch-icon" href="/assets/icon-v2-180.png">
<link rel="alternate" type="application/rss+xml" title="Shadinota Tech Blog" href="{SITE}/blog/feed.xml">
<meta name="theme-color" content="#09090b">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Shadinota Tech">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og}">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Sora:wght@600;700&display=swap" rel="stylesheet">
{extra_ld}
<style>{CSS}</style>
</head>"""


def nav(active="blog"):
    return f"""<body>
<div class="bgfx" aria-hidden="true"></div>
<header class="top"><nav class="main wrap" aria-label="Main">
<a class="brand" href="/"><img src="/assets/logo-white-256.webp" alt="" width="36" height="36">Shadinota Tech</a>
<div class="links"><a href="/#apps">Apps</a><a href="/cardcraft/">CardCraft</a><a href="/blog/" class="{'on' if active=='blog' else ''}">Blog</a><a href="/#contact">Contact</a></div>
<a class="btn" style="min-height:40px;padding:8px 16px;font-size:14px" href="{PLAY}" target="_blank" rel="noopener">Get CardCraft</a>
</nav></header>"""


FOOT = """<footer><div class="wrap"><span>© {y} Shadinota Tech, Khulna, Bangladesh</span>
<span><a href="/">Home</a> · <a href="/blog/">Blog</a> · <a href="/cardcraft/">CardCraft</a> · <a href="/privacy.html">Privacy</a> · <a href="/blog/feed.xml">RSS</a></span></div></footer>
</body></html>"""

CTA_HTML = f"""<aside class="cta" aria-label="CardCraft app">
<img src="/assets/cc-icon.webp" alt="CardCraft icon" width="72" height="72" loading="lazy">
<div><h3 class="h">Make these ID cards on your phone</h3>
<p>CardCraft has 185 templates, Excel/CSV import, bulk photos and print-ready A4 sheets with cut marks at 300 DPI. Free to start, works offline.</p>
<a class="btn pri" href="{PLAY}" target="_blank" rel="noopener">Get CardCraft on Google Play</a></div></aside>"""


def card(p):
    return f"""<a class="pcard" href="/blog/{p['slug']}/">
<img src="/blog/{p['slug']}/og.png" alt="" loading="lazy" width="1200" height="630">
<div class="pb"><span class="c">{html.escape(p['category'])}</span><h3 class="h">{html.escape(p['title'])}</h3>
<p>{html.escape(p['description'])}</p><span class="d">{fmt_date(p['date'])} · {p['minutes']} min read</span></div></a>"""


def post_page(p, related):
    url = f"{SITE}/blog/{p['slug']}/"
    og = f"{url}og.png"
    body = p["html"]
    # inline CTA marker or after the 3rd h2
    if "<!-- cta -->" in body:
        body = body.replace("<!-- cta -->", CTA_HTML, 1)
    else:
        parts = re.split(r"(?=<h2 )", body)
        if len(parts) > 4:
            parts.insert(4, CTA_HTML)
            body = "".join(parts)
    ld = [{
        "@context": "https://schema.org", "@type": "BlogPosting",
        "headline": p["title"], "description": p["description"],
        "image": og, "datePublished": p["date"], "dateModified": p["updated"],
        "author": {"@type": "Person", "name": AUTHOR, "jobTitle": AUTHOR_ROLE, "url": SITE + "/", "worksFor": {"@type": "Organization", "name": "Shadinota Tech", "url": SITE + "/"}},
        "publisher": {"@type": "Organization", "name": "Shadinota Tech", "logo": {"@type": "ImageObject", "url": SITE + "/assets/icon-v2-512.png"}},
        "mainEntityOfPage": url, "keywords": ", ".join(p["keywords"]), "wordCount": p["words"], "inLanguage": "en",
    }, {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": SITE + "/blog/"},
            {"@type": "ListItem", "position": 3, "name": p["title"], "item": url},
        ]}]
    if p["faq"]:
        ld.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]})
    ld_html = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in ld)
    toc = "".join(f'<a href="#{i}">{html.escape(n)}</a>' for i, n in p["toc"])
    upd = f" · Updated {fmt_date(p['updated'])}" if p["updated"] != p["date"] else ""
    rel = "".join(card(r) for r in related)
    return head(f"{p['title']} | Shadinota Tech", p["description"], url, og, ld_html) + nav() + f"""
<main class="wrap">
<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/blog/">Blog</a> / {html.escape(p['category'])}</nav>
<header class="post-head"><span class="cat">{html.escape(p['category'])}</span>
<h1 class="h">{html.escape(p['title'])}</h1>
<p class="lede">{html.escape(p['description'])}</p>
<div class="meta"><span>By {AUTHOR}</span><span><time datetime="{p['date']}">{fmt_date(p['date'])}</time>{upd}</span><span>{p['minutes']} min read</span></div></header>
<div class="layout">
<article class="prose">{body}
{CTA_HTML if '<aside class="cta"' not in body else ''}
<div class="author"><img src="/assets/logo-white-256.webp" alt="" width="52" height="52"><div><b>{AUTHOR}</b>Founder of Shadinota Tech and developer of CardCraft – ID Card Maker. He builds tools in Khulna, Bangladesh, that help schools, offices and print shops make and print ID cards every day.</div></div>
</article>
<aside class="toc" aria-label="On this page"><b>On this page</b>{toc}
<div class="side-cta"><p>Make and print ID cards from your phone.</p><a class="btn pri" style="width:100%;min-height:40px;font-size:14px" href="{PLAY}" target="_blank" rel="noopener">Get CardCraft</a></div></aside>
</div>
{'<section class="related"><h2 class="h">Keep reading</h2><div class="grid">' + rel + '</div></section>' if rel else ''}
</main>
""" + FOOT.format(y=dt.date.today().year)


def index_page(posts):
    cards = "".join(card(p) for p in posts) or "<p>First article coming soon.</p>"
    ld = {"@context": "https://schema.org", "@type": "Blog", "name": "Shadinota Tech Blog", "url": SITE + "/blog/",
          "blogPost": [{"@type": "BlogPosting", "headline": p["title"], "url": f"{SITE}/blog/{p['slug']}/", "datePublished": p["date"]} for p in posts[:20]]}
    return head("ID Card Guides & Tips – Shadinota Tech Blog", "Practical guides on designing, printing and managing ID cards for schools, offices, factories and events — from the team behind CardCraft.", SITE + "/blog/", SITE + "/assets/og-v2.jpg",
                f'<script type="application/ld+json">{json.dumps(ld)}</script>', og_type="website") + nav() + f"""
<main class="wrap">
<section class="bloghero"><span class="cat">Blog</span><h1 class="h">ID card guides that actually help.</h1>
<p>Sizes, layouts, printing, photos and workflows for schools, offices, factories and events — written by the team that builds CardCraft.</p></section>
<div class="grid">{cards}</div>
</main>
""" + FOOT.format(y=dt.date.today().year)


def rss(posts):
    items = "".join(f"""<item><title>{html.escape(p['title'])}</title><link>{SITE}/blog/{p['slug']}/</link><guid>{SITE}/blog/{p['slug']}/</guid>
<pubDate>{dt.datetime.fromisoformat(p['date']).strftime('%a, %d %b %Y 06:00:00 +0600')}</pubDate><description>{html.escape(p['description'])}</description></item>
""" for p in posts[:30])
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel><title>Shadinota Tech Blog</title><link>{SITE}/blog/</link>
<description>ID card guides and tips from the team behind CardCraft.</description><language>en</language>
{items}</channel></rss>
"""


def sitemap(posts):
    today = dt.date.today().isoformat()
    last_post = posts[0]["updated"] if posts else today
    rows = []
    for path, freq, pri in STATIC_PAGES:
        lm = last_post if path in ("/", "/blog/") else None
        rows.append(f"<url><loc>{SITE}{path}</loc>{f'<lastmod>{lm}</lastmod>' if lm else ''}<changefreq>{freq}</changefreq><priority>{pri}</priority></url>")
    for p in posts:
        rows.append(f"<url><loc>{SITE}/blog/{p['slug']}/</loc><lastmod>{p['updated']}</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>")
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(rows) + "\n</urlset>\n"


def home_block(posts):
    idx = ROOT / "index.html"
    s = idx.read_text(encoding="utf-8")
    start, end = "<!-- BLOG:START -->", "<!-- BLOG:END -->"
    if start not in s:
        return
    cards = "".join(f"""<a class="bcard rv" href="/blog/{p['slug']}/"><img src="/blog/{p['slug']}/og.png" alt="" width="1200" height="630"><div><span>{html.escape(p['category'])} · {p['minutes']} min</span><h3 class="h">{html.escape(p['title'])}</h3></div></a>""" for p in posts[:3])
    block = f"""{start}
  <section class="sec" id="blog" style="padding-top:0">
    <div class="wrap">
      <div class="sec-head rv"><div><p class="eyebrow">From the blog</p><h2 class="h">Guides for better ID cards</h2></div><a class="btn" href="/blog/">All articles</a></div>
      <div class="bgrid">{cards}</div>
    </div>
  </section>
  {end}"""
    s = re.sub(re.escape(start) + r".*?" + re.escape(end), block if posts else f"{start}{end}", s, flags=re.S)
    idx.write_text(s, encoding="utf-8")

# ---------------------------------------------------------------- main

def main():
    posts = []
    today = dt.date.today().isoformat()
    for f in sorted(SRC.glob("*.md")):
        p = parse(f)
        if p["draft"] or p["date"] > today:
            continue
        p["html"], p["toc"] = render_md(p["body_md"])
        p["faq"] = extract_faq(p["body_md"])
        p["words"] = words(p["body_md"])
        p["minutes"] = max(1, math.ceil(p["words"] / 220))
        posts.append(p)
    posts.sort(key=lambda p: p["date"], reverse=True)
    slugs = [p["slug"] for p in posts]
    if len(slugs) != len(set(slugs)):
        sys.exit("duplicate slugs")
    for p in posts:
        others = [o for o in posts if o["slug"] != p["slug"]]
        others.sort(key=lambda o: (o["category"] != p["category"], o["date"] < p["date"]))
        d = OUT / p["slug"]
        d.mkdir(parents=True, exist_ok=True)
        if not (d / "og.png").exists() or os.environ.get("REBUILD_OG"):
            make_og(p["title"], p["category"], d / "og.png")
        (d / "index.html").write_text(post_page(p, others[:3]), encoding="utf-8")
    OUT.mkdir(exist_ok=True)
    (OUT / "index.html").write_text(index_page(posts), encoding="utf-8")
    (OUT / "feed.xml").write_text(rss(posts), encoding="utf-8")
    (ROOT / "sitemap.xml").write_text(sitemap(posts), encoding="utf-8")
    home_block(posts)
    print(f"built {len(posts)} post(s): " + ", ".join(slugs))


if __name__ == "__main__":
    main()
