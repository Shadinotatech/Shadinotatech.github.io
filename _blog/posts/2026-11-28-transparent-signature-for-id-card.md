---
title: Transparent Signature for ID Card: Make, Size and Place It
description: How to make a transparent signature for an ID card from a phone photo: pen and paper, removing the white, exact size in mm and pixels, placement and fixes.
slug: transparent-signature-for-id-card
date: 2026-11-28
category: Design
keywords: transparent signature for id card, how to make signature transparent, signature png for id card, authorized signature on id card, signature size on id card, remove white background from signature
---

<div class="keytakeaways" markdown="1">
<b>Key takeaways</b>

- **A transparent signature is a PNG with no paper behind the ink**, so it sits cleanly on any card colour. A JPG cannot be transparent, which is why it prints as a white box.
- **Sign big, with a bold pen.** Sign about 50–70 mm wide on plain white paper with a 0.7–1.0 mm black gel or felt-tip pen, then shrink it. A thin ballpoint line almost disappears at card size.
- **Print size on a CR80 card: about 25–35 mm wide and 8–12 mm tall.** At 300 DPI a 30 × 10 mm signature is 354 × 118 px, so keep the trimmed source at least 700 px wide.
- **Remove the white in two steps:** first push the paper to pure white (contrast or levels), then make white transparent. Skipping step one leaves a grey halo.
- **Place it on the back, bottom right, over the signatory's printed name and title,** inside the 3 mm safe zone, and keep the file private.
</div>

The authorised signature is the small detail that makes an ID card look official, and also the one that most often looks wrong: a white rectangle on a coloured card, a grey smudge around the ink, or a hairline scribble you can barely see.

This guide shows how to make a transparent signature for an ID card from a phone photo, with the exact print size in mm and pixels, where to place it, and a fix for every common problem.

## What is a transparent signature, and why does an ID card need one?

A digital image is a grid of pixels. A normal photo of a signature contains two things: the ink and the paper. When you place that photo on a card with a coloured band, a tinted background or a pattern, the paper comes along and shows up as a white or greyish block.

A **transparent signature** keeps the ink pixels and deletes the paper pixels. The file stores an extra "alpha" channel that says, pixel by pixel, how see-through it is. Only some formats can store this:

| Format | Can be transparent? | Good for ID cards? | Notes |
|---|---|---|---|
| PNG | Yes | **Best choice** | Lossless, keeps sharp ink edges, supported everywhere |
| JPG / JPEG | No | No | Always has a solid background; compression adds blotches around ink |
| WebP | Yes | Usable | Fine if your design tool accepts it; PNG is safer |
| SVG (vector) | Yes | Only if traced well | Infinitely sharp, but auto-tracing often loses pen pressure detail |
| PDF | Yes | Only inside a finished card file | Not a practical format for the signature on its own |

So when anyone asks for a "signature PNG for an ID card", they mean the same thing: the ink alone, with a transparent background, saved as PNG.

<figure>
<svg viewBox="0 0 800 320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Two CR80 card backs drawn to scale at 4 pixels per millimetre. On the left a JPG signature shows a white box over the tinted background. On the right a transparent PNG signature sits cleanly on the tint, 30 by 10 millimetres, inside the 3 millimetre safe zone.">
<rect width="800" height="320" fill="#0f0f12"/>
<defs>
<pattern id="tint" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
<rect width="10" height="10" fill="#e9ecff"/>
<rect width="4" height="10" fill="#dde2ff"/>
</pattern>
</defs>
<g font-family="sans-serif">
<g transform="translate(30,40)">
<rect width="342" height="216" rx="13" fill="url(#tint)"/>
<rect x="12" y="12" width="318" height="192" rx="4" fill="none" stroke="#4fe3c1" stroke-dasharray="4 4"/>
<rect x="24" y="26" width="200" height="9" rx="2" fill="#3f3f46"/>
<rect x="24" y="46" width="160" height="7" rx="2" fill="#71717a"/>
<rect x="24" y="60" width="180" height="7" rx="2" fill="#71717a"/>
<rect x="24" y="74" width="130" height="7" rx="2" fill="#71717a"/>
<rect x="202" y="120" width="124" height="48" fill="#ffffff" stroke="#c4c4cc"/>
<path d="M214 152 c10 -26 18 -26 16 -4 c-2 16 10 -18 22 -14 c10 4 -6 18 6 14 c14 -6 18 -22 28 -12 c8 8 -4 14 10 8 c10 -4 14 -8 22 -6" fill="none" stroke="#1f2a5a" stroke-width="2.4" stroke-linecap="round"/>
<line x1="204" y1="174" x2="324" y2="174" stroke="#3f3f46" stroke-width="1"/>
<text x="264" y="188" font-size="9" fill="#27272a" text-anchor="middle">Name, Title</text>
</g>
<text x="201" y="282" font-size="13" fill="#e4e4e7" text-anchor="middle">JPG or photo: white box shows</text>
<text x="201" y="300" font-size="11" fill="#a1a1aa" text-anchor="middle">The paper comes along with the ink</text>
<g transform="translate(428,40)">
<rect width="342" height="216" rx="13" fill="url(#tint)"/>
<rect x="12" y="12" width="318" height="192" rx="4" fill="none" stroke="#4fe3c1" stroke-dasharray="4 4"/>
<rect x="24" y="26" width="200" height="9" rx="2" fill="#3f3f46"/>
<rect x="24" y="46" width="160" height="7" rx="2" fill="#71717a"/>
<rect x="24" y="60" width="180" height="7" rx="2" fill="#71717a"/>
<rect x="24" y="74" width="130" height="7" rx="2" fill="#71717a"/>
<rect x="204" y="126" width="120" height="40" fill="none" stroke="#8b9cff" stroke-dasharray="3 3"/>
<path d="M214 152 c10 -26 18 -26 16 -4 c-2 16 10 -18 22 -14 c10 4 -6 18 6 14 c14 -6 18 -22 28 -12 c8 8 -4 14 10 8 c10 -4 14 -8 22 -6" fill="none" stroke="#1f2a5a" stroke-width="2.4" stroke-linecap="round"/>
<line x1="204" y1="174" x2="324" y2="174" stroke="#3f3f46" stroke-width="1"/>
<text x="264" y="188" font-size="9" fill="#27272a" text-anchor="middle">Name, Title</text>
<text x="264" y="120" font-size="9" fill="#4f5bd5" text-anchor="middle">30 × 10 mm</text>
</g>
<text x="599" y="282" font-size="13" fill="#e4e4e7" text-anchor="middle">Transparent PNG: ink only</text>
<text x="599" y="300" font-size="11" fill="#a1a1aa" text-anchor="middle">Dashed teal line = 3 mm safe zone</text>
</g>
</svg>
<figcaption>The back of a landscape CR80 card (85.6 × 54 mm) drawn to scale. The same signature as a JPG (left) and as a transparent PNG (right), sized 30 × 10 mm in the bottom-right corner.</figcaption>
</figure>

## Step 1: sign so the result survives shrinking

Most bad card signatures are ruined before anyone opens an app. The signature is photographed at its natural size and then reduced to about half, so every line gets half as thick.

A worked example makes the point:

- A signature written **60 mm wide** with a **0.7 mm gel pen** leaves a line of roughly 0.6–0.7 mm. Shrunk to 30 mm on the card, the line is about **0.35 mm**, or 4 pixels at 300 DPI. It prints solid.
- The same signature with a **fine ballpoint** leaves a line of roughly 0.3 mm. Shrunk by half, it becomes about **0.15 mm**, under 2 pixels. On an inkjet or a laminated paper card it breaks into a dotted, grey scribble.

So, before you photograph:

1. **Use plain white paper** (A4 printer paper is fine). No ruled lines, no letterhead, no stamp behind the signature.
2. **Use a 0.7–1.0 mm black gel pen or felt-tip.** Dark blue also works if you want the signature to stay blue; avoid light blue ballpoint and pencil.
3. **Sign 50–70 mm wide**, in one confident stroke, the way the signatory signs official letters. Sign three or four times and pick the best one.
4. **Let the ink dry** for a minute so a gel pen does not smear or shine.

## Step 2: photograph the signature properly

The goal is a photo where the paper is evenly bright and the ink is evenly dark. That makes removing the white almost automatic.

- **Light:** daylight from a window, or a ceiling light behind you, with no direct sun. Avoid the phone flash; it makes a hot spot in the middle and a dark ring at the edges.
- **No shadow:** hold the phone so your hand and the phone do not shade the page. A shadow across the paper is the main cause of grey halos later.
- **Straight on:** keep the phone parallel to the paper, about 20–30 cm away, so the signature is not skewed.
- **Fill the frame sensibly:** the signature should take up at least half of the photo's width. A modern phone camera then gives you well over 1,000 pixels of signature, which is plenty.
- **Focus:** tap on the ink before you shoot, and check the photo at full zoom. Soft edges cannot be fixed later.

If you already know how to take good ID photos with a phone, the same light rules apply; our guide to [taking an ID card photo with your phone](/blog/how-to-take-id-card-photo-with-phone/) covers window light and shadows in more detail.

## Step 3: how to make a signature transparent

Removing the paper is really two jobs. First, make every paper pixel **pure white** and every ink pixel **clearly dark**. Second, turn white into transparent. If you only do the second job, the light-grey paper pixels survive as a soft halo around the ink.

### Option A: inside your ID card app

The quickest route is an ID card maker that does both jobs for you. In [CardCraft](/cardcraft/), you sign on paper, take a photo with the in-app camera, and the signature comes out transparent, ready to sit on any template colour. You set it once for the institute, and every card in that institute uses it.

### Option B: free desktop software (GIMP)

GIMP is free and gives you full control:

1. Open the photo, crop tightly around the signature (leave 2–3 mm of space) and straighten it if needed.
2. Use **Colors → Levels** (or Curves) and drag the white point left until the paper turns completely white. Drag the black point right a little so the ink is solid.
3. Use **Colors → Desaturate** if you want pure black ink, or skip it to keep blue.
4. Use **Color to Alpha** with white as the colour. Older versions show it under the Colors menu; GIMP 3 also offers it under **Layer → Transparency**. See the [GIMP documentation](https://docs.gimp.org/en/gimp-filter-color-to-alpha.html) for the options.
5. **File → Export As**, choose a `.png` name, and export.

### Option C: Word or PowerPoint

If the card is designed in Word or PowerPoint, insert the photo, then use **Picture Format → Color → Set Transparent Color** and click the paper. This makes one exact colour transparent, so it works only when the paper is already pure white. Brighten the photo first (Picture Format → Corrections) or you will see speckles of paper left behind.

### Option D: online background removers

Many websites remove a signature background in one click. They work, but think before you upload: a signature is sensitive, and you are handing a clean copy of it to a third party. If you use one, choose a service whose privacy policy says uploads are deleted, and never use one for a signature that also signs cheques or contracts.

> **Tip:** Whatever tool you use, check the result on a dark background before saving. Grey fringes and leftover paper specks are invisible on white and obvious on navy.

## What size should a signature be on an ID card?

On a standard CR80 card (85.6 × 54 mm), the signature block usually sits in the bottom-right corner of the back. It needs to be big enough to look like a real signature and small enough to leave room for the return text, validity and contact lines. Our guide to [what to put on the back of an ID card](/blog/what-to-put-on-the-back-of-an-id-card/) shows how that space is shared.

| Card | Signature width | Signature height | Pixels at 300 DPI | Minimum source size (2×) |
|---|---|---|---|---|
| CR80 landscape back | 30 mm | 10 mm | 354 × 118 px | 709 × 236 px |
| CR80 portrait back | 25 mm | 8–9 mm | 295 × 100 px | 591 × 201 px |
| CR80, signature on the front | 22 mm | 7 mm | 260 × 83 px | 520 × 165 px |
| 4 × 3 in badge | 35 mm | 12 mm | 413 × 142 px | 827 × 283 px |
| A6 or 4R event pass | 40 mm | 14 mm | 472 × 165 px | 945 × 331 px |

The pixel figures are simply millimetres ÷ 25.4 × 300. The last column doubles them, because a source file with twice the pixels you print keeps edges crisp after resizing and leaves room if you later make the signature a little larger. If you need every other card size in mm, inches and pixels, see the [ID card size chart](/blog/id-card-size-cr80-mm-inches-pixels/).

Two practical rules sit on top of the table:

- **Height matters more than width.** A long signature can be 35 mm wide, but if it drops below about 7 mm tall, it reads as a scribble.
- **Never stretch.** Scale the signature proportionally. A squashed signature looks forged, which is the opposite of what it is for.

## Where to put the authorised signature on an ID card

The usual layout, used on most office, school and factory cards, is:

- **Side:** the back. This keeps the front free for the photo, name and ID number. Put it on the front only on single-sided cards.
- **Position:** bottom right, inside the 3 mm safe zone, away from any slot punch or clip.
- **Under it:** a thin line, then the signatory's printed name and title, for example "Md. Rafiqul Islam, Headmaster" or "Manager, HR & Admin", at 6.5–7 pt.
- **Label:** "Authorised signature", or in Bangla "কর্তৃপক্ষের স্বাক্ষর". Use one label, not both a label and a title, if space is tight.
- **Who signs:** the person who has authority to issue cards: the principal or head teacher at a school, the head of HR or the managing director at a company, the event director for event passes. One signatory for the whole batch keeps cards consistent.

On an [employee ID card](/blog/employee-id-card-design-what-to-include/) the signature normally sits on the back next to the validity date. On student cards it is the principal's or head teacher's signature, and at madrasas it may be the muhtamim's.

### Signature over a stamp or seal

Many organisations in Bangladesh add the office seal next to or partly under the signature. If you do, make the seal a separate transparent PNG and put it **behind** the signature in a lighter tone, so the ink stays readable. Do not photograph the signature on top of a real stamp; the two cannot be separated cleanly afterwards.

## Fixing common transparent signature problems

| Problem | Cause | Fix |
|---|---|---|
| White box behind the signature | Saved as JPG, or the PNG was flattened | Export again as PNG with transparency; check the design tool did not add a background |
| Grey or coloured halo around the ink | Paper was not pure white before removing white | Raise brightness or use Levels first, then remove white again |
| Ink looks faint or broken | Thin pen, or signature shrunk too much | Re-sign larger with a 0.7–1.0 mm pen |
| Jagged, blocky edges | Source too small, then enlarged | Re-photograph closer; keep at least 2× the print pixels |
| Blue or yellow tint on the ink | Mixed light (window plus warm bulb) | Shoot in one light source, or desaturate to black |
| Shadow stripe across part of the signature | Hand or phone shaded the paper | Re-shoot with light from the side or behind you |
| Specks of paper left around the ink | Set Transparent Color on a non-white photo | Brighten first, or use a tool with a tolerance setting |

## Checklist before you print the batch

Run through this once with a single test card, printed at 100% scale, before you print the whole batch:

- The signature file is a **PNG with a transparent background**, tested on a dark colour.
- The ink is **solid and dark** at full zoom, with no grey fringe.
- On the printed card it measures roughly **25–35 mm wide and 8–12 mm tall**.
- It sits **inside the 3 mm safe zone**, clear of the slot punch and holder clip.
- The **printed name and title** under it are spelled correctly.
- The signature is **not stretched** or squashed.
- The same signature is used on **every card in the batch**.
- The original file is **stored privately**, not on a shared drive or website.

## Keep the signature file safe

A clean transparent signature is easy to copy, so treat the file like a key. Keep it in the ID card app or one private folder, do not email it around or post it in group chats, and do not publish it on the website. When the signatory leaves, replace the signature on new cards and decide whether old cards stay valid until their expiry date.

A signature on an ID card shows that *your organisation* issued the card. It is not a legal identity document, and it must never be used to imitate anyone else's signature or a government document.

<!-- cta -->

## Frequently asked questions

### How do I make my signature transparent for free?

Sign on plain white paper with a dark, bold pen and photograph it in even light. Brighten the photo until the paper is pure white, then use a free tool such as GIMP's Color to Alpha, or Word's Set Transparent Color, and save it as a PNG. An ID card app that removes the paper from a signature photo does both steps for you.

### Why does my signature show a white box on the ID card?

The image still contains the paper. Either it was saved as a JPG, which cannot be transparent, or the white was never removed. Save the signature as a PNG with a transparent background and place that file on the card.

### What is the best size for a signature on an ID card?

On a standard CR80 card, about 30 mm wide and 10 mm tall on a landscape back, or 25 × 8–9 mm on a portrait back. At 300 DPI that is roughly 354 × 118 pixels, so keep the source image at least twice that size.

### Should the signature be black or blue on an ID card?

Either works if the ink is dark. Black gives the strongest contrast on every background colour and survives photocopying, so it is the safer default. Keep the signatory's usual blue only if it is a dark blue and the card background is light.

### Who should sign an ID card?

The person with authority to issue the cards: the principal or head teacher for a school, the head of HR or the managing director for a company, and the organiser for event passes. Print their name and title under the signature so anyone checking the card knows who issued it.

### Is it safe to put a scanned signature on ID cards?

It is common and generally acceptable for an organisation's own cards, but the file can be copied. Keep the transparent PNG private, use it only for card printing, and avoid using the same image that signs cheques or contracts.
