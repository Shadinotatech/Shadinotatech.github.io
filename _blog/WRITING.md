# Blog writing guide (shadinotatech.com)

This is the standard every article must meet. The daily publishing task follows it exactly.

## Who we write for
Admins, teachers, HR/office staff, print-shop owners and event organisers — in Bangladesh and worldwide — who need to design, print or manage ID cards. Plain, practical English. No fluff, no hype.

## What makes an article worth publishing (Google helpful-content / E-E-A-T)
- **Solve the searcher's task completely**, so they never need to go back to Google. Lead with the answer.
- **Original, specific value**: exact numbers (mm, px, DPI, pt), worked examples, tables, checklists, ready-to-copy text, decision rules. Prefer our own calculations and real workflow experience over generic advice.
- **Accuracy**: verify every fact that could be wrong (sizes, standards, prices, policies) with a fresh web search on the day of writing. Never invent statistics, studies, quotes or prices. If a number varies, give a range and say where it comes from (e.g. "listings on BDStall in 2026"). Link 1–3 authoritative sources (standards bodies, Wikipedia for ISO standards, manufacturer docs).
- **No copying**: write everything in our own words. Never reproduce sentences from other sites.
- **Local edge**: where relevant, include Bangladesh/South-Asia context (schools & madrasas, garment factories, BDT prices, Bangla names, A4 print shops) — competitors rarely cover it.
- **Honest product mentions**: CardCraft is mentioned where it genuinely helps (1–3 times + the automatic CTA box). Only claim features listed on /cardcraft/ (185 templates, 24 colour schemes, Employee/Student/Badge/Event/Visitor/Membership/Photo ID types, several institutes, CR80/4×3 badge/3R/4R/A6/custom mm sizes, portrait & landscape, front & back, Excel/CSV import & export, bulk photos, in-app camera with crop/light/plain background, transparent signature from a photo, dashboard for missing photos/expiring cards, A4 sheets with cut marks, 300 DPI PDF/PNG/ZIP, offline, English & Bangla, free up to 10 people; Pro ৳129/month, ৳799/year, ৳1,999 lifetime). Never say it makes government IDs.
- **Never** help with fake/forged/government identity documents. Our topic is an organisation's own cards.

## Structure (Markdown in `_blog/posts/YYYY-MM-DD-slug.md`)
```
---
title: <50–65 chars, primary keyword near the start, natural>
description: <140–160 chars, the promise of the article, includes primary keyword>
slug: <from plan.json>
date: YYYY-MM-DD
category: <Printing | Design | Guides | Photos | Workflows | Industries | Buying guides>
keywords: <primary>, <3–6 secondary>
---
```
1. `<div class="keytakeaways" markdown="1">` box with **Key takeaways** (3–5 bullets that answer the query on their own).
2. Short intro (2–4 sentences): the problem and what the reader will get. Primary keyword once, naturally.
3. 5–9 `##` sections in the order a reader needs them. Use question-style H2s where they match real searches. `###` for sub-steps.
4. At least **one table** and **one checklist or numbered procedure**. Add an inline SVG diagram (`<figure><svg …></svg><figcaption>…</figcaption></figure>`, dark background `#0f0f12`, accent `#4fe3c1` / `#8b9cff`, drawn to scale where it is about sizes/layout) when a picture explains it better than words.
5. Optional tip boxes with `> **Tip:** …`.
6. Put `<!-- cta -->` once, before the FAQ (the build inserts the CardCraft box there).
7. `## Frequently asked questions` with 4–6 `###` questions (real "People also ask"-style queries) and 2–4 sentence answers. These become FAQ schema automatically.

## Length & style
- 1,600–2,500 words of genuinely useful content. Depth over padding: cut any sentence that does not help.
- Short paragraphs (1–4 sentences), active voice, second person ("you"), metric first with inches in brackets where useful.
- UK/international spelling is fine; be consistent within an article.
- No "In today's fast-paced world", no "Conclusion" section that repeats everything, no emoji, no keyword stuffing.

## Internal links
- Link to 1–3 **already published** posts (check `_blog/posts/`) where it helps the reader, using descriptive anchor text, plus `/cardcraft/` once if relevant. Never link to posts that do not exist yet.
- After publishing, add one contextual link **from** the most related older post **to** the new post (edit that older post's Markdown and bump its `updated:` date).

## Publish checklist
1. `python3 _blog/build.py` runs without errors.
2. Open the generated `blog/<slug>/index.html` text and re-read it once for facts, typos and broken links.
3. Update `_blog/plan.json`: set the post's `status` to `published` and add `"published": "YYYY-MM-DD"`.
4. Commit with a clear message and push to `main` (Cloudflare Pages deploys automatically in ~1 minute).
5. Check `https://shadinotatech.com/blog/<slug>/` returns 200.
