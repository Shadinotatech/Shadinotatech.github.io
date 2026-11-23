---
title: ID Cards from Excel Data: Prepare, Import and Bulk Print
description: Make ID cards from Excel data without retyping: the column layout, formulas that catch errors, photo file naming, CSV UTF-8 for Bangla and bulk printing steps.
slug: make-id-cards-from-excel-list
date: 2026-11-23
category: Workflows
keywords: id card from excel data, bulk id card maker, id card csv import, mass id card printing, id card mail merge, excel to id card
---

<div class="keytakeaways" markdown="1">
<b>Key takeaways</b>

- Making ID cards from Excel data works when the sheet is **one header row, one row per person, one column per card field**, with no merged cells, blank rows or totals.
- Store **ID numbers and phone numbers as text**. Excel drops leading zeros (`0045` becomes `45`, `01712…` loses its `0`) and shows long numbers in scientific notation.
- Name every photo after the person's **ID number** (`S-2027-0045.jpg`), not their name. IDs are unique; names repeat and get misspelled.
- Save as **CSV UTF-8** if any field is in Bangla; a plain CSV can turn it into question marks.
- Run a five-minute check (duplicates, empty cells, over-long names, missing photos) before you import. Fixing 3 rows in a sheet beats reprinting 30 cards.
</div>

If you have a staff or student list in a spreadsheet, you should never type it again into an ID card designer. Making ID cards from Excel data is faster and far more accurate, but only if the sheet is clean before it goes in.

This guide shows the exact column layout, the Excel formulas that catch problems, how to name photos so they match the right person, and the steps from import to a printed A4 stack. It works the same in Excel, Google Sheets or a phone spreadsheet app.

## Why import instead of typing?

Retyping names on a phone keyboard is where most card errors start, and every typo is a reprint. A spreadsheet also usually exists already: HR has the payroll list, the school office has the admission register, the event team has the registration export.

Importing gives you three things typing does not:

1. **One source of truth.** The card shows exactly what is in the official list, so the spelling on the card matches the spelling in the register.
2. **Proofreading at a glance.** Scanning a column of 400 names on a computer screen is much easier than flicking through 400 card previews.
3. **Reuse next year.** Change the class column and the validity date, re-import, and the renewal batch is ready.

## How should the spreadsheet be laid out?

Every bulk ID card tool, from Word mail merge to a mobile app, reads a sheet the same way: the first row is the column names and every row below it is one card. Anything else in the sheet confuses the import.

| Column | Example | Keep it as | Why it matters |
|---|---|---|---|
| ID number | `S-2027-0045` | Text | Unique key for photo matching; leading zeros must survive |
| Full name | `Nusrat Jahan` | Text, trimmed | Exactly as it should print; no double spaces |
| Name (Bangla) | `নুসরাত জাহান` | Text, saved as UTF-8 | Only if the card is bilingual |
| Designation / Class | `Class 7` | Text | Keep one spelling per value (`Class 7`, not also `VII`) |
| Department / Section | `B` | Text | Short values fit better on CR80 |
| Blood group | `O+` | Text from a fixed list | Pick from 8 values only: A+, A−, B+, B−, AB+, AB−, O+, O− |
| Phone | `01712345678` | Text | Excel removes the leading `0` from numbers |
| Valid until | `31-12-2027` | One date format for the whole column | Mixed formats import as wrong dates |
| Photo file | `S-2027-0045.jpg` | Text (formula) | Tells you which photo belongs to the row |

Rules that save the most trouble:

- **One header row only.** No school name banner in row 1, no logo, no title. Put those in the card design instead.
- **No merged cells, no blank rows, no subtotal rows.** A blank row often ends the import early; a merged cell shifts data into the wrong column.
- **Short, plain column names** like `Name`, `ID`, `Class`. Avoid line breaks inside header cells.
- **One sheet per card type.** Staff and students usually have different fields; keep them in separate files.

> **Tip:** If your card tool can export its own list, add one person by hand, export, and use that file as your template. The columns are then in exactly the order the tool expects.

## How do you stop Excel breaking ID and phone numbers?

This is the most common reason bulk cards come out wrong. Excel treats anything that looks like a number as a number, so:

- `0045` becomes `45`.
- A Bangladesh mobile number `01712345678` becomes `1712345678`.
- With the country code, `8801712345678` (13 digits) may display as `8.80171E+12`.
- Anything over 15 digits, such as some long registration numbers, loses its final digits for good: Excel keeps only 15 significant digits and turns the rest into zeros. Microsoft documents this in [Keeping leading zeros and large numbers](https://support.microsoft.com/en-us/office/keep-leading-zeros-and-large-numbers-1bf7b935-36e1-4985-842f-5dfa51f85fe7).

Fix it **before** you paste or type the data:

1. Select the ID and phone columns.
2. Right-click → **Format Cells** → **Text** → OK.
3. Now paste or type the values. Already-damaged numbers will not come back by changing the format; re-paste them from the original source.

For a single cell you can also type an apostrophe first (`'0045`). If your IDs are plain serial numbers and you only need padding, a helper column with `=TEXT(A2,"0000")` turns `45` into `0045`; copy it and use **Paste Special → Values** to make it permanent.

## How should you name the photos?

Photos are the part of a bulk job that goes wrong silently: the card prints fine, just with the wrong face. Use a naming rule that cannot be confused.

- **Name each photo after the ID number**, e.g. `S-2027-0045.jpg`. Two students can both be called Mohammad Rahim; they cannot share an ID.
- Use **only letters, numbers and hyphens** in file names. No spaces, no Bangla characters, no brackets.
- Keep **one file type** (JPG is fine) and keep the extension lowercase so `.JPG` and `.jpg` do not count as different files.
- Put all photos for one batch in **one folder**.

Add a formula column so the sheet itself says which photo each row needs:

```
=A2&".jpg"
```

Then, if you can see the folder listing on a computer, paste the file names into another sheet and check each row with `=IF(COUNTIF(Photos!A:A,I2)=0,"MISSING","")`. Every "MISSING" is a person to photograph before print day. Our guide to [taking ID card photos with a phone](/blog/how-to-take-id-card-photo-with-phone/) covers how to run a fast photo session so the gaps get filled in one go.

<figure>
<svg viewBox="0 0 640 230" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Flow: spreadsheet row with ID S-2027-0045 matches photo file S-2027-0045.jpg, which produces one ID card, then an A4 sheet of 10 cards">
<rect width="640" height="230" fill="#0f0f12"/>
<g font-family="Inter,sans-serif" font-size="12" fill="#e4e4e7">
<rect x="20" y="40" width="170" height="120" rx="6" fill="#18181b" stroke="#4fe3c1"/>
<text x="105" y="30" text-anchor="middle" fill="#a1a1aa">1. Spreadsheet row</text>
<text x="32" y="66" fill="#4fe3c1">ID</text><text x="80" y="66">S-2027-0045</text>
<text x="32" y="90" fill="#4fe3c1">Name</text><text x="80" y="90">Nusrat Jahan</text>
<text x="32" y="114" fill="#4fe3c1">Class</text><text x="80" y="114">7 · B</text>
<text x="32" y="138" fill="#4fe3c1">Photo</text><text x="80" y="138">S-2027-0045.jpg</text>
<rect x="225" y="55" width="90" height="90" rx="6" fill="#18181b" stroke="#8b9cff"/>
<circle cx="270" cy="88" r="16" fill="#8b9cff" fill-opacity=".8"/><rect x="245" y="108" width="50" height="26" rx="13" fill="#8b9cff" fill-opacity=".8"/>
<text x="270" y="30" text-anchor="middle" fill="#a1a1aa">2. Photo by ID</text>
<text x="270" y="168" text-anchor="middle" font-size="11">S-2027-0045.jpg</text>
<rect x="350" y="57" width="128" height="81" rx="5" fill="#f4f4f5"/>
<rect x="350" y="57" width="128" height="18" rx="5" fill="#4fe3c1"/><rect x="360" y="84" width="30" height="38" rx="2" fill="#8b9cff"/>
<rect x="398" y="88" width="66" height="7" fill="#3f3f46"/><rect x="398" y="102" width="46" height="5" fill="#71717a"/><rect x="398" y="113" width="56" height="5" fill="#71717a"/>
<text x="414" y="30" text-anchor="middle" fill="#a1a1aa">3. One card</text>
<g transform="translate(520,22)">
<rect width="100" height="141" fill="#f4f4f5" rx="2"/>
<g fill="#4fe3c1" fill-opacity=".85">
<rect x="8" y="4" width="40.8" height="25.7" rx="1.5"/><rect x="51" y="4" width="40.8" height="25.7" rx="1.5"/>
<rect x="8" y="31" width="40.8" height="25.7" rx="1.5"/><rect x="51" y="31" width="40.8" height="25.7" rx="1.5"/>
<rect x="8" y="58" width="40.8" height="25.7" rx="1.5"/><rect x="51" y="58" width="40.8" height="25.7" rx="1.5"/>
<rect x="8" y="85" width="40.8" height="25.7" rx="1.5"/><rect x="51" y="85" width="40.8" height="25.7" rx="1.5"/>
<rect x="8" y="112" width="40.8" height="25.7" rx="1.5"/><rect x="51" y="112" width="40.8" height="25.7" rx="1.5"/>
</g>
<text x="50" y="160" text-anchor="middle" fill="#a1a1aa">4. A4 × 10</text>
</g>
<g stroke="#a1a1aa" stroke-width="1.5" fill="none"><path d="M192 100h28"/><path d="M318 100h28"/><path d="M481 100h34"/></g>
<text x="320" y="210" text-anchor="middle" fill="#a1a1aa" font-size="11">The ID number is the key that ties the row, the photo and the printed card together.</text>
</g>
</svg>
<figcaption>The ID number links each spreadsheet row to its photo and its card. The A4 sheet is drawn to scale.</figcaption>
</figure>

## Five-minute data check before you import

Run these on a copy of the sheet. Each one takes a few seconds and catches a whole class of reprints. They work the same in Google Sheets.

| Check | Formula (row 2, copy down) | What it catches |
|---|---|---|
| Duplicate ID | `=IF(COUNTIF(A:A,A2)>1,"DUP","")` | Two people with one number, or one person entered twice |
| Extra spaces | `=IF(B2<>TRIM(B2),"SPACES","")` | Double spaces and trailing spaces that shift centred text |
| Empty required field | `=IF(COUNTBLANK(A2:D2)>0,"EMPTY","")` | Rows missing an ID, name, class or section |
| Name too long | `=IF(LEN(B2)>26,"LONG","")` | Names that will shrink or wrap on a CR80 card |
| Bad blood group | `=IF(COUNTIF($L$2:$L$9,F2)=0,"CHECK","")` | `O +`, `o+`, `0+` and other variants (list the 8 valid values in L2:L9) |

Then use **Data → Filter** on each helper column to see only the flagged rows. The 26-character limit is a rule of thumb for one line of name text across a landscape CR80 card at a readable size; check your own template, since a portrait layout fits fewer characters.

Two more habits that help:

- Use **Data → Data Validation → List** for fields with fixed values (class, section, blood group, department). People then pick from a dropdown instead of typing a new spelling.
- **Sort** by class, section or department just before saving. Cards print in that order, which makes handing them out much faster.

## Save in the right format: XLSX or CSV UTF-8

Most tools accept either an Excel file (`.xlsx`) or a CSV. If you use CSV, the encoding matters.

- In Excel, choose **File → Save As → CSV UTF-8 (Comma delimited)**. The older plain "CSV (Comma delimited)" option can replace Bangla, Arabic or accented characters with question marks.
- Google Sheets exports CSV as UTF-8 by default (**File → Download → Comma-separated values**).
- Open the saved CSV once in a text editor or re-open it to make sure the Bangla names still read correctly.
- Remember that a CSV stores only values. The leading zeros survive only if the cells were text before saving, and re-opening the CSV in Excel and saving again can strip them, so make the CSV the last step.

## Importing and printing: the step-by-step

Here is the full run for a typical batch, whatever tool you use.

1. **Freeze the data.** Agree with HR or the office that this copy is final for this batch. Late changes go in a "next batch" sheet.
2. **Run the five checks** above and fix every flagged row.
3. **Save** as XLSX or CSV UTF-8 and copy the file and the photo folder to the device you will design on.
4. **Import the list** and look at the first and last few people. If names appear in the ID column, the column mapping is off; fix it before going further.
5. **Add the photos** in bulk, then look for anyone still without a photo.
6. **Proof a sample**: one long name, one short name, one person from each department or class, and every role that uses a different colour.
7. **Export a 300 DPI PDF** of A4 sheets with cut marks and print one test sheet at 100% scale. Measure a card: it should be 85.6 × 54 mm. Our guide to [printing ID cards on A4 paper](/blog/how-to-print-id-cards-on-a4-paper/) covers scaling, duplex alignment and cutting.
8. **Print the batch**, cut, and tick names off the sheet as cards are handed out.
9. **Save the final list** (export it) with the batch date, so next year's renewal starts from clean data.

In [CardCraft](/cardcraft/), step 4 is importing an Excel or CSV file, step 5 is adding photos one by one or in bulk, and the dashboard shows who still has no photo and whose card expires within 30 days. You can export the list again at any time, which covers step 9.

## Other ways to turn Excel into ID cards

The method above uses a dedicated ID card tool. Two desktop routes are also common:

- **Word mail merge.** Fine for text-only badges: set up a label sheet, connect the Excel list and insert merge fields. Photos are harder: Word needs a nested `INCLUDEPICTURE` field that points to each image's full file path, and the pictures often need a manual refresh (F9) before they show. See Microsoft's notes on the [IncludePicture field](https://support.microsoft.com/en-au/word/field-codes-includepicture-field).
- **Design software data merge** (InDesign, Illustrator variables, Inkscape extensions, Canva-style bulk create). Powerful if you already use the software, but you set the card size, bleed and A4 imposition yourself.

All routes need the same clean sheet.

## Worked example: 412 factory workers in one afternoon

A garment factory HR officer has a payroll export with 412 workers. Here is how the batch goes from export to print.

1. The export has a company banner in rows 1–3 and a total at the bottom. She deletes them, keeping one header row.
2. Worker numbers like `00871` had already lost their zeros. She formats the column as Text and re-pastes from the payroll system.
3. The duplicate check flags 2 rows: one worker entered twice after a transfer between lines. One row is deleted, leaving 411.
4. Blood group values include `B +`, `b+` and blanks. She sets a dropdown, fixes 37 cells and leaves 6 blanks for workers who do not know theirs, then checks how her template shows an empty field.
5. Photo check: 388 of 411 photos exist; 23 workers are photographed at the gate next morning.
6. Sorted by section and line, saved as CSV UTF-8 because section names include Bangla.

At 10 landscape cards per A4 sheet, 411 cards need 42 sheets (41 full sheets plus one with a single card). With a test sheet and a few spares, 45 sheets of card stock is a sensible order.

## Checklist: is your sheet ready?

- One header row, one row per person, no merged cells or blank rows
- ID and phone columns formatted as Text, leading zeros visible
- No duplicate IDs (COUNTIF check is clean)
- No extra spaces in names (TRIM check is clean)
- Fixed-value fields use one spelling each
- Every row has a photo named `<ID>.jpg`, or the gaps are listed
- Long names reviewed against your template
- Saved as XLSX or CSV UTF-8, Bangla text checked
- Sorted in the order you will hand cards out
- A dated copy kept for next year's renewal

<!-- cta -->

## Frequently asked questions

### How do I make ID cards from an Excel list?

Clean the sheet first: one header row, one row per person, ID and phone columns stored as text. Save it as XLSX or CSV UTF-8, import it into an ID card maker or a Word mail merge, add photos named by ID number, proof a sample and print 300 DPI A4 sheets at 100% scale.

### Can I add photos to ID cards automatically from Excel?

Excel itself does not hold photos for a merge; it holds the file names. Name each photo after the person's ID number and keep all photos in one folder, then use a tool that adds photos in bulk or a Word `INCLUDEPICTURE` field that points to each file. Check for missing photos before printing.

### Why does Excel remove the zero from my ID numbers?

Excel treats `0045` as the number 45 and drops the leading zero. Format the column as Text before you enter or paste the data, or type an apostrophe before the value. Phone numbers such as `01712345678` need the same treatment.

### Should I use CSV or XLSX for ID card import?

Either works if your tool accepts it. XLSX keeps text formatting more reliably, while CSV is simpler and accepted almost everywhere. If you use CSV and any names are in Bangla or another non-Latin script, save as CSV UTF-8, or the text may turn into question marks.

### How many ID cards can I print from one Excel sheet?

There is no fixed limit in the spreadsheet itself; the limit is your tool and your printer. Plan paper by dividing the number of people by cards per sheet: at 10 CR80 cards per A4 sheet, 400 people need 40 sheets, plus a few for tests and reprints.
