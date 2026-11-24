---
title: ID Card Size in Pixels, mm and Inches (CR80 and Every Badge Size)
description: The exact ID card size in pixels at 300 and 600 DPI, plus CR80, CR79 and CR100 in mm and inches, bleed, safe zone, thickness and badge sizes in one table.
slug: id-card-size-cr80-mm-inches-pixels
date: 2026-11-16
updated: 2026-11-24
category: Design
keywords: id card size in pixels, cr80 card size, standard id card size in mm, id card size 300 dpi, cr79 cr100 size, id card bleed and safe zone
---

<div class="keytakeaways" markdown="1">
<b>Key takeaways</b>

- The standard ID card (CR80, ISO/IEC 7810 ID-1) is **85.6 × 53.98 mm**, or **3.370 × 2.125 in**.
- In pixels that is **1011 × 638 px at 300 DPI** and **2022 × 1275 px at 600 DPI**. For a portrait card, swap them: 638 × 1011 px.
- If your printer or print shop wants bleed, add **3 mm on each side**: the canvas becomes **91.6 × 60 mm, about 1082 × 708 px at 300 DPI**.
- Keep text and photos inside a **3 mm safe zone**, which leaves about **79.6 × 48 mm (940 × 567 px)** for important content.
- Standard PVC cards are **0.76 mm (30 mil)** thick with corners rounded to about **3.2 mm**.
</div>

Almost every "my ID card looks blurry" or "it doesn't fit the holder" problem starts with the wrong canvas size. This page gives you the ID card size in pixels, millimetres and inches for every common format, explains bleed and safe zones with a to-scale diagram, and shows you how to set up the file correctly in any design app.

Bookmark it: the tables below are the ones we use ourselves when building templates.

## The standard ID card size (CR80) at a glance

The card in your wallet, your bank card, most staff and student ID cards: they are all the same size. The international standard [ISO/IEC 7810](https://en.wikipedia.org/wiki/ISO/IEC_7810) calls it **ID-1**. Card printer makers and suppliers call it **CR80**.

| Measurement | Value |
|---|---|
| Millimetres | 85.60 × 53.98 mm (usually rounded to 85.6 × 54) |
| Inches | 3.370 × 2.125 in (often quoted as 3⅜ × 2⅛, which is 3.375) |
| Pixels at 150 DPI | 506 × 319 px (screen preview only) |
| Pixels at 300 DPI | **1011 × 638 px** |
| Pixels at 600 DPI | **2022 × 1275 px** |
| Aspect ratio | about 1.586 : 1 |
| Corner radius | 2.88–3.48 mm in the standard; about 3.2 mm (⅛ in) in practice |
| Thickness | 0.76 mm ± 0.08 mm (30 mil) |

**Portrait or landscape does not change the size.** A vertical card is simply 53.98 × 85.6 mm, or 638 × 1011 px at 300 DPI.

### Why do some sites say 1013 × 638 px?

Because they start from the rounded inch figure. 3.375 in × 300 = 1012.5, which rounds to 1013. The true ID-1 width is 85.60 mm, which is 3.370 in, and 3.370 × 300 = 1011. The difference is about 0.2 mm on the printed card, so either canvas works in practice. What matters is that you print at 100% scale and keep important content away from the edges.

## ID card size in pixels at 300 and 600 DPI

Pixels only mean something together with a resolution. The formula is:

**pixels = millimetres ÷ 25.4 × DPI**

So for the CR80 width at 300 DPI: 85.6 ÷ 25.4 × 300 = 1011 px.

Which DPI should you choose?

- **300 DPI** is the minimum for anything that will be printed. Text, logos and photos look sharp at normal viewing distance. This is what we recommend for A4 inkjet and laser printing, and it is what CardCraft exports.
- **600 DPI** is worth it for very small text (under 6 pt), fine security patterns or microtext, and for some direct-to-card printers that print at higher resolution. It also makes files four times larger.
- **72 or 96 DPI** is screen resolution. A CR80 card at 72 DPI is only 243 × 153 px. If you design at that size, the print will look soft or pixelated, however good the photo was.

> **Tip:** In Photoshop, GIMP or Photopea, create the document in **millimetres** (85.6 × 54 mm) and set the resolution to 300 pixels/inch. The app calculates the pixels for you and you cannot get the ratio wrong.

## Every common card and badge size in one table

CR80 covers most ID cards, but schools, events and access-control systems use a handful of other sizes. Here they all are, landscape dimensions first. For portrait, swap width and height.

| Format | Millimetres | Inches | Pixels at 300 DPI | Pixels at 600 DPI | Typical use |
|---|---|---|---|---|---|
| **CR80 / ID-1** | 85.6 × 53.98 | 3.370 × 2.125 | 1011 × 638 | 2022 × 1275 | Staff, student, membership and bank cards |
| CR79 | 83.9 × 52.1 | 3.303 × 2.051 | 991 × 615 | 1982 × 1231 | Adhesive cards stuck onto thick proximity (clamshell) cards |
| CR100 | 98.6 × 66.8 | 3.88 × 2.63 | 1165 × 789 | 2329 × 1578 | Larger badges, events, parking passes |
| ID-2 | 105 × 74 | 4.134 × 2.913 | 1240 × 874 | 2480 × 1748 | Some national documents and visas (not a format to imitate) |
| 4 × 3 in badge | 101.6 × 76.2 | 4 × 3 | 1200 × 900 | 2400 × 1800 | Conference and trade-show badges in plastic pouches |
| 3R | 88.9 × 127 | 3.5 × 5 | 1050 × 1500 | 2100 × 3000 | Event passes printed on photo paper |
| 4R | 101.6 × 152.4 | 4 × 6 | 1200 × 1800 | 2400 × 3600 | Large event and backstage passes |
| A6 | 105 × 148 | 4.13 × 5.83 | 1240 × 1748 | 2480 × 3496 | Event passes cut from A4 (4 per sheet) |

A few notes on the less common sizes:

- **CR79** exists because thick proximity cards (the kind used for door access) are hard to print on directly. You print a slightly smaller adhesive card and stick it on, so it does not overhang the edges.
- **CR100** is about 42% larger in area than CR80. Many desktop card printers cannot feed it, so check before you design for it.
- **3R, 4R and A6** are paper sizes rather than card sizes, but they are very common for event passes because any photo lab or print shop can print them. In Bangladesh, 3R and 4R are everyday photo-print sizes at local studios. For name font sizes, role colours and QR placement on these formats, see our [event badge design guide](/blog/event-badge-design-and-sizes/).

## Bleed, trim and safe zone: what they mean and how big they are

These three terms decide whether your card looks professional after it is cut.

- **Trim size** is the finished card: 85.6 × 54 mm.
- **Bleed** is extra background that extends past the trim line, so a slightly off cut never leaves a white sliver. The usual amount is **3 mm per side** (print shops in Bangladesh, India and Europe) or **⅛ in, 3.175 mm** (US suppliers).
- **Safe zone** is the area inside the trim where all important content must stay. Use **3 mm** from every edge. Corners are rounded, cutting drifts, and a slot punch for a lanyard can take a bite out of the top.

<figure>
<svg viewBox="0 0 520 330" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="CR80 card drawn to scale showing the 3 mm bleed outside the trim line and the 3 mm safe zone inside it">
<rect width="520" height="330" fill="#0f0f12"/>
<g transform="translate(77,40) scale(4)">
<rect x="0" y="0" width="91.6" height="60" fill="#8b9cff" fill-opacity=".25"/>
<rect x="3" y="3" width="85.6" height="54" rx="3.2" fill="#1c1c22" stroke="#4fe3c1" stroke-width=".4"/>
<rect x="6" y="6" width="79.6" height="48" fill="none" stroke="#8b9cff" stroke-width=".3" stroke-dasharray="1.2 0.8"/>
<rect x="10" y="12" width="20" height="25" rx="1" fill="#4fe3c1" fill-opacity=".5"/>
<rect x="35" y="14" width="40" height="4" rx="1" fill="#f4f4f5" fill-opacity=".8"/>
<rect x="35" y="22" width="30" height="3" rx="1" fill="#a1a1aa"/>
<rect x="35" y="28" width="34" height="3" rx="1" fill="#a1a1aa"/>
</g>
<g font-family="Inter,sans-serif" font-size="12">
<text x="77" y="30" fill="#8b9cff">Bleed: 91.6 × 60 mm (1082 × 708 px at 300 DPI)</text>
<text x="77" y="300" fill="#4fe3c1">Trim line: 85.6 × 54 mm (1011 × 638 px)</text>
<text x="77" y="318" fill="#a1a1aa">Dashed: 3 mm safe zone, 79.6 × 48 mm (940 × 567 px)</text>
</g>
</svg>
<figcaption>A CR80 card to scale (1 mm = 4 units). Background runs into the bleed; text and photo stay inside the dashed safe zone.</figcaption>
</figure>

The numbers you will actually type into a design app:

| Canvas | Millimetres | Pixels at 300 DPI | Pixels at 600 DPI |
|---|---|---|---|
| Trim only (no bleed) | 85.6 × 54 | 1011 × 638 | 2022 × 1275 |
| With 3 mm bleed | 91.6 × 60 | 1082 × 708 | 2164 × 1417 |
| With ⅛ in bleed | 91.95 × 60.33 | 1086 × 713 | 2172 × 1425 |
| Safe zone (content area) | 79.6 × 48 | 940 × 567 | 1880 × 1133 |

**Do you need bleed at all?** Only if your design has colour or an image running to the edge and someone is going to cut the card. If you send files to a card printer that prints edge-to-edge on pre-cut PVC, ask the supplier: many want the trim size only, with no crop marks. If you print several cards on A4 and cut them yourself, bleed plus cut marks is the safer choice, as we explain in our guide to [printing ID cards on A4 paper](/blog/how-to-print-id-cards-on-a4-paper/).

## Card thickness: 30 mil and the alternatives

Thickness is measured in **mil** (one thousandth of an inch, 0.0254 mm). It does not affect your design file, but it affects which printer and holder you can use.

| Thickness | Millimetres | Common use |
|---|---|---|
| 10 mil | 0.25 mm | Adhesive-backed cards (often CR79), labels |
| 13–20 mil | 0.33–0.51 mm | Gym and loyalty cards, transit tickets |
| **30 mil** | **0.76 mm** | **Standard ID, access, student and bank cards** |
| 55–65 mil | 1.40–1.65 mm | Luggage tags, thick proximity (clamshell) cards |

For staff and student cards, choose 30 mil. It is the ISO ID-1 thickness, fits every standard holder and badge reel, and almost every card printer feeds it. A paper card laminated in 125-micron pouches comes out thinner than PVC, but it is the same width and height, so it still fits standard holders.

## Photo, logo and text sizes that work on a CR80 card

Getting the canvas right is half the job. The other half is making sure the elements on it are big enough to print and read. These are the starting points we use for templates at 300 DPI:

| Element | Suggested size | At 300 DPI |
|---|---|---|
| Photo (landscape card) | about 22 × 28 mm | 260 × 331 px |
| Photo (portrait card) | about 26 × 32 mm | 307 × 378 px |
| Logo in header | 8–12 mm tall | 94–142 px tall |
| Person's name | 9–12 pt | readable at arm's length |
| Other details (ID, department) | 6.5–8 pt | do not go below 6 pt |
| QR code | at least 15 × 15 mm | 177 × 177 px |

The source photo should be at least as large as the photo box in pixels, and ideally twice as large, so cropping does not soften it. Any modern phone camera is far above that.

## How to set up an ID card file correctly (step by step)

Use this procedure in any design app, whether that is Photoshop, Illustrator, Canva, Inkscape or a phone app:

1. **Decide orientation.** Landscape suits wallet and clip use; portrait suits lanyards.
2. **Create the canvas in mm or inches, not pixels.** Enter 85.6 × 54 mm (or 54 × 85.6 for portrait).
3. **Set resolution to 300 DPI** (600 if you have tiny text or a high-resolution card printer).
4. **Add 3 mm bleed** on every side if the background touches the edges and the card will be cut. Your canvas is now 91.6 × 60 mm.
5. **Draw guides 3 mm inside the trim line.** Put every name, number, photo and logo inside them.
6. **Leave room for a slot punch** if cards will hang from a lanyard: keep the top 10 mm (portrait) clear of text.
7. **Place photos at full resolution** and check that they are not upscaled.
8. **Export as PDF or PNG at 100% scale.** For a print shop, a PDF with fonts embedded is safest.
9. **Print one test on plain paper at 100% / Actual size** and measure it: it should be 85.5–86 mm wide.

If you use CardCraft on Android, the sizes are already set up: you pick CR80, a 4×3 badge, 3R, 4R, A6 or a custom size in mm, choose portrait or landscape, and it exports print-ready 300 DPI PDF or PNG files (and A4 sheets with cut marks), so you never have to type pixel values.

## Common sizing mistakes and how to avoid them

- **Designing at screen resolution.** A 600 × 380 px canvas looks fine on a monitor but prints at under 180 DPI. Start at 1011 × 638 px or more.
- **Stretching to fit.** If a template is 1000 × 700 px, it is not a CR80 ratio. Squeezing it into 85.6 × 54 mm distorts faces and logos. Fix the canvas, not the print.
- **"Fit to page" when printing.** It shrinks every card by a few percent. Always print at 100%.
- **Text right at the edge.** Rounded corners and cutting tolerance will clip it. Stay inside the 3 mm safe zone.
- **Using A4 paper size math for Letter.** If your print shop uses Letter (8.5 × 11 in) paper, layouts made for A4 will not line up. In Bangladesh A4 is the norm, but check foreign templates.
- **Mixing CR79 and CR80.** Designing for one and printing on the other leaves a 1.7 mm overhang or a white edge.

## Checklist: is your ID card file print-ready?

- Canvas is 85.6 × 54 mm (or 54 × 85.6 for portrait), or 91.6 × 60 mm with bleed.
- Resolution is 300 DPI or higher: at least 1011 × 638 px for the trim area.
- Background extends to the bleed edge if it touches the card edge.
- All text, photos, logos and QR codes are at least 3 mm inside the trim line.
- Smallest text is 6 pt or larger.
- Photos are not upscaled and look sharp at 100% zoom.
- Top area is clear if a slot punch will be used.
- A test print measured 85.5–86 mm wide.

<!-- cta -->

## Frequently asked questions

### What is the size of an ID card in pixels?

A standard CR80 ID card is 1011 × 638 pixels at 300 DPI, or 2022 × 1275 pixels at 600 DPI. For a vertical card, swap the numbers to 638 × 1011 px. Some sources say 1013 × 638 px because they round the width to 3.375 inches; the difference is too small to notice once printed.

### What is the standard ID card size in mm?

The standard size is 85.6 × 53.98 mm, usually written as 85.6 × 54 mm. This is the ID-1 format from ISO/IEC 7810, also called CR80, and it is the same size as a bank card.

### What is the ID card size in inches?

A CR80 card is 3.370 × 2.125 inches, commonly rounded to 3⅜ × 2⅛ inches (3.375 × 2.125). A 4 × 3 inch badge and the CR100 (3.88 × 2.63 inches) are larger formats used mainly for events.

### What is the difference between CR79, CR80 and CR100?

CR80 is the standard 85.6 × 54 mm card. CR79 is slightly smaller, about 83.9 × 52.1 mm, and is usually an adhesive card stuck onto a thick proximity card. CR100 is larger, about 98.6 × 66.8 mm, and is used for event and parking badges, but fewer printers accept it.

### How much bleed does an ID card need?

Use 3 mm on each side, which makes the canvas 91.6 × 60 mm (about 1082 × 708 px at 300 DPI). Some US suppliers ask for ⅛ inch instead, which is almost the same. If you print on pre-cut PVC cards, check with the supplier, since many want the trim size only.

### How thick is a standard ID card?

A standard PVC ID card is 30 mil, or 0.76 mm, thick. That is the ISO ID-1 thickness and the one that fits standard holders and card printers. Thinner 10–20 mil cards are used for adhesive labels and loyalty cards.
