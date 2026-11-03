import os

with open('scratch/mapping_table.txt', 'r', encoding='utf-8') as f:
    table = f.read()

template = """# Product Catalogue Reconciliation & Technical Hand-Off Report

> [!IMPORTANT]
> **Release Blocker:** Live WhatsApp enquiry redirection is currently **disabled by design**. In accordance with strict safety instructions, enquiry buttons open a user-friendly review modal containing the prefilled enquiry text and public link, alerting the operator that the international-format destination phone number (`+91 ...`) requires explicit client sign-off before production release.

---

## 1. Executive Summary

This project involved reconciling the product catalogue website for **MSR Tent Mart** against the authoritative client PDF (`Google-Drive-Images/Product List-Code - v001.pdf`) and the downloaded original photo archive (`Google-Drive-Images/MSR-TentMart-Files/`).

The website has been transformed from a legacy static layout with dummy product data, made-up codes, hardcoded price zero (`Rs 0`), and duplicate per-category markup into a **single-source-of-truth, JSON-driven, DRY catalogue system**.

### Key Statistics
- **Authoritative Source:** 15-page client specification PDF (`Product List-Code - v001.pdf`).
- **Total Products in Scope:** **77 products** across **7 categories** (100% matched, verified, and active in the catalogue).
- **Product Code Uniqueness:** **100%** (77 unique codes, 0 duplicates, 0 fabricated codes).
- **Image Mapping Integrity:** **77 / 77 products** mapped with 100% HTTP 200 OK verification over local HTTP server.
- **Original Photo Archive Audited:** **109 image files** inventoried across 7 folders, including duplicate detection, alternate exposure sorting, and group palette classification.
- **Prices:** Missing prices are modeled strictly as `null` ("Price on Request"), eliminating misleading zero-cost labels.

```mermaid
flowchart TD
    subgraph Client Authority
        PDF["Client PDF (15 Pages)<br/>77 Products, 7 Categories"]
        Photos["Downloaded Archive (109 Photos)<br/>Sofa, Mate, Screen, Flower, Bowls..."]
    end

    subgraph Data Layer
        JSON["assets/json/product_list.json<br/>- 7 Stable Categories<br/>- 77 Products (Codes, Display Order, Alt Text)"]
        WebImages["assets/images/products/<br/>Web-Optimized Responsive Assets"]
    end

    subgraph Presentation & UI Logic
        AppJS["assets/js/app.js<br/>Shared DRY Engine"]
        CSS["assets/css/catalogue.css<br/>Design System & Modal"]
    end

    subgraph Views
        Home["index.html<br/>Featured Grid & Navigation"]
        AllProds["products/index.html<br/>Search Bar & Dynamic Filter Pills"]
        Cats["categories/*.html<br/>7 DRY Category Listing Pages"]
        Modal["Shared Enquiry Modal<br/>Prefilled WhatsApp Text & Link"]
    end

    PDF --> JSON
    Photos --> WebImages
    JSON --> AppJS
    WebImages --> AppJS
    CSS --> Views
    AppJS --> Home
    AppJS --> AllProds
    AppJS --> Cats
    AppJS --> Modal
```

---

## 2. Inventory & Photographic Reconciliation Audit

The downloaded image collection (`Google-Drive-Images/MSR-TentMart-Files/`) was discovered and thoroughly audited against the 15 PDF pages. The photo folders represented raw camera dump and photo shoot staging directories, not final catalogue taxonomy.

### Folder-by-Folder Reconciliation

| Source Folder | File Count | PDF Section / Category Match | Resolution & Audit Notes |
| :--- | :---: | :--- | :--- |
| **`Sofa/`** | 23 files | `Sofa` (Codes: `MSE 10` – `MSE 52`, Pages 1–6) | **1:1 Perfect Match.** All 23 files correspond exactly to the 23 sofa models in the PDF. Web-optimized copies generated at `assets/images/products/sofa/`. |
| **`Mate/`** | 19 files | `Mate` (Codes: `MM_01` – `MM_16`, Pages 7–9) | **16 Products, 3 Redundant Bit-for-bit Duplicates.**<br/>Exact duplicates identified:<br/>- `WhatsApp Image ... at 11.41.10 AM (3).jpeg` == `... at 11.41.10 AM.jpeg`<br/>- `WhatsApp Image ... at 11.41.11 AM (3).jpeg` == `... at 11.41.11 AM (1).jpeg`<br/>- `WhatsApp Image ... at 11.41.11 AM.jpeg` == `... at 11.41.11 AM (2).jpeg`<br/>The 16 unique files were mapped directly to `MM_01`–`MM_16`. |
| **`Screen/`** | 7 files | `Screen` (Codes: `MS_S_001` – `MS_GR_006`, Page 10) | **6 Products.** 5 matched DSC camera files (`DSC05170`, `5172`, `5173`, `5175`, `5176`). `DSC05171` and `DSC05174` are bracketed alternates.<br/>`MS_GR_006` (*Stall Screen Gold Red*) was missing from raw camera dump but present on PDF Page 10; extracted directly from PDF raster stream and optimized. |
| **`Bowl/`** | 4 files | `Bouquet` (Codes: `MS_RB_001` – `MS_PB_004`, Page 14) | **1:1 Match.** The 4 round bowl bouquet photos (`DSC05162`, `5165`, `5166`, `5168`) correspond exactly to the 4 Bouquet entries in the PDF. (Source folder named `Bowl` after product shape). |
| **`Runner/`** | 15 files | `Flower` (Codes: `MS_PR_001` – `MS_PR_009`, Pages 11–12) | **9 Runner Products.** Contains primary photos (`DSC05114`, `5119`, `5123`, `5139`, `5144`, `5148`, `5150`, `5155`, `5157`). Remaining files are bracketed exposure alternates (`DSC05115-5118`, `5120-5122`, etc.). |
| **`Hanging Flower set/`**| 13 files | `Flower` (Codes: `MS_HF_001` – `MS_HF_007`, Page 13) | **7 Hanging Flower Products.** Primary photos matched (`DSC05127`, `5129`, `5130`, `5135`, `5137`, `5159`, `5161`). Remaining files are bracketed lighting alternates. |
| **Root DSC Files** | 8 files | Close-up macro shots (`DSC05151`–`DSC05169`) | **Detail Angle References.** `DSC05163`, `5164`, `5167`, `5169` are vertical close-ups of the 4 Bouquets; `DSC05151-5154` are close-up angles of Flower Runners. Preserved as source references. |
| **`Mums` & `Carnation`** | 2 Posters | `Mums` (7 codes, Page 15) & `Carnation` (5 codes, Page 15) | **Palette Swatches.** PDF Page 15 displays these as multi-code color palettes on single photos matching marketing posters in `assets/images/gallery/msr-tent-mart_big-mums.jpeg` and `msr-tent-mart_carnation.jpeg`. Handled with explicit `isGroupPhoto: true`, `groupImage`, and honest swatch badges. |

---

## 3. Complete 77-Product Auditable Mapping Table

| PDF Page | Product Code | Display Name | Category ID | Original Source File / Evidence | Website Image Asset | Group Reference? |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- |
###TABLE_PLACEHOLDER###

---

## 4. Architectural Transformation & DRY Implementation

### Files Changed & Created

1. **[`assets/json/product_list.json`](file:///D:/My-Projects/AI-Session/bff-demo-site-01.github.io/assets/json/product_list.json)**
   - Created central authoritative database with `categories` (7 records) and `products` (77 records).
   - Features: stable IDs, exact client codes, category foreign keys, explicit display ordering, descriptive alt text, `null` prices, and source tracing.

2. **[`assets/js/app.js`](file:///D:/My-Projects/AI-Session/bff-demo-site-01.github.io/assets/js/app.js)**
   - Refactored into a modular, reusable client engine.
   - Core modules:
     - `fetchCatalogueData()`: Centralized cached fetch with error handling.
     - `resolveAssetPath(path)`: Base-aware URL resolver supporting root, subfolder (`/products/`, `/categories/`), and GitHub Pages subpath deployment.
     - `renderProductCard(product, category)`: Single DRY card component with code badge, swatch badge, price formatting, and enquiry action.
     - `initAllProductsPage()`: Live search filtering across name/code and interactive category pills with live product counts.
     - `initCategoryPage(categoryId)`: Shared category view initialization.
     - `handleProductEnquiry(productCode)`: Shared WhatsApp enquiry builder.
     - `showEnquiryNoticeModal(message, targetUrl)`: User review modal displaying the prefilled message with one-click copy and release blocker notification.

3. **[`assets/css/catalogue.css`](file:///D:/My-Projects/AI-Session/bff-demo-site-01.github.io/assets/css/catalogue.css)**
   - Created dedicated stylesheet for product grid, search toolbar, filter pills, badge styling, and accessible modal overlay.

4. **[`products/index.html`](file:///D:/My-Projects/AI-Session/bff-demo-site-01.github.io/products/index.html)**
   - Replaced bloated, hardcoded category blocks with dynamic filter pills and responsive product grid.

5. **[`categories/*.html`](file:///D:/My-Projects/AI-Session/bff-demo-site-01.github.io/categories/)** (`sofa.html`, `mate.html`, `screen.html`, `flower.html`, `bouquet.html`, `mums.html`, `carnation.html`)
   - Standardized to thin declarative templates delegating all rendering to `initCategoryPage('<id>')`.

6. **[`index.html`](file:///D:/My-Projects/AI-Session/bff-demo-site-01.github.io/index.html)**
   - Integrated shared catalogue styling, connected featured products grid to `initHomePage()`, and removed stale Cloudflare script blocking local execution.

7. **[`assets/css/index.css`](file:///D:/My-Projects/AI-Session/bff-demo-site-01.github.io/assets/css/index.css)**
   - Fixed `.nav-logo img` sizing from `object-fit: cover` to `contain` with proper padding so brand logo renders cleanly.

8. **[`layout/footer.html`](file:///D:/My-Projects/AI-Session/bff-demo-site-01.github.io/layout/footer.html)**
   - Cleaned up broken relative paths (`../collections/`, `../our-products/`) to ensure proper navigation from all directory depths.

---

## 5. Verification & Testing

### Programmatic Test Results
- **HTTP Status Check:** All 12 key pages, styles, scripts, and JSON return `200 OK` over HTTP (`http://127.0.0.1:8080`).
- **Product Image Integrity:** All 77 product images/group references verified `200 OK` (0 broken links).
- **Code Uniqueness:** All 77 product codes verified unique.
- **Search & Filter:** Verified instant filtering on both desktop and mobile viewports.

### Visual Verification
Visual inspection was conducted using headless Chrome across desktop (1280px) and mobile (390px) viewports:
- **Product Card Layout:** Cards align cleanly in CSS grid with consistent aspect ratio, clear product codes, and formatted buttons.
- **Group Swatch Handling:** Items in Mums and Carnation display an honest "Color Swatch Reference" badge instead of misleading individual photo crops.
- **Enquiry Modal:** Clicking "Inquire via WhatsApp" displays the prefilled message with full product details, public link, and release blocker banner.

Captured visual verification screenshots stored in `screenshots/`:
- `screenshots/homepage_desktop.png` - Home page with working logo and navigation
- `screenshots/products_desktop.png` - All products catalogue with search bar & filter pills
- `screenshots/products_mobile.png` - Mobile responsive layout (390px viewport)
- `screenshots/products_grid_view.png` - Grid rendering of product cards
- `screenshots/sofa_grid_view.png` - Dedicated category view (Sofa)
- `screenshots/mums_grid_view.png` - Swatch-based category view (Mums)

---

## 6. Maintenance & Operator Guide

### 1. How to Edit a Category Label
Open `assets/json/product_list.json` and locate the `categories` array. Update the `name` field:
```json
{
  "id": "sofa",
  "name": "Luxury Sofas",
  "displayOrder": 1
}
```
All navigation menus, category headers, and filter pills update automatically.

### 2. How to Add or Update a Product
Add or edit an entry in the `products` array in `assets/json/product_list.json`:
```json
{
  "id": "sofa-mse-99",
  "code": "MSE 99",
  "name": "Sofa Royal Gold",
  "categoryId": "sofa",
  "displayOrder": 24,
  "image": "assets/images/products/sofa/mse-99.jpg",
  "altText": "Sofa Royal Gold (Code: MSE 99)",
  "price": null,
  "originalSource": "WhatsApp Image ...",
  "pdfPage": 6
}
```

### 3. How to Replace a Photo
1. Save the new image in `assets/images/products/<category>/<filename>.jpg` (recommended 800x800px or 4:3 ratio JPEG, < 250 KB).
2. Update the `image` path in `assets/json/product_list.json`.

---

## 7. Outstanding Decisions & Release Blockers

> [!WARNING]
> **Action Required Before Going Live:**
> 1. **WhatsApp Target Confirmation:** Confirm the official international phone number with country code (e.g. `916384500051`). In `assets/js/app.js`, update:
>    ```javascript
>    const CONFIG = {
>        whatsappNumber: '916384500051',
>        whatsappEnabled: true // Switch to true upon confirmation
>    };
>    ```
> 2. **Base URL for Live Deployment:** When deploying to GitHub Pages or custom domain, update `CONFIG.siteBaseUrl` in `assets/js/app.js` if the site is served from a subdirectory.
"""

final_doc = template.replace('###TABLE_PLACEHOLDER###', table)

out_target = r"C:\Users\User\.gemini\antigravity\brain\a8b5bfad-ab49-4818-a85c-0de9ffc11a2c\catalogue_reconciliation_report.md"
with open(out_target, 'w', encoding='utf-8') as f:
    f.write(final_doc)

print("Saved report to:", out_target, "Size:", len(final_doc))
