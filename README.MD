# MSR Tent Mart — Website

Static website for MSR Tent Mart, a supplier of event decoration materials.

No build step needed. No frameworks. Plain HTML, CSS, and JavaScript.

---

## Folder Layout

```
bff-demo-site-01.github.io/
├── index.html                  ← Home page (only page at root)
├── products/index.html         ← All products page
├── categories/                 ← One page per product category
│   ├── bouquet.html
│   ├── carnation.html
│   ├── flower.html
│   ├── mate.html
│   ├── mums.html
│   ├── screen.html
│   └── sofa.html
├── about/index.html            ← Placeholder (content pending)
├── contact/index.html          ← Placeholder (content pending)
├── 404.html                    ← Custom 404 error page
│
├── assets/
│   ├── css/
│   │   ├── variables-theme.css ← All CSS variables (colors, fonts, radii, shadows)
│   │   ├── globals.css         ← Shared utility and layout styles
│   │   ├── index.css           ← Home page styles
│   │   ├── catalogue.css       ← Product card and modal styles
│   │   └── template-page.css   ← Pattern for new content page CSS
│   ├── js/
│   │   └── app.js              ← All site logic and product rendering
│   ├── json/
│   │   └── product_list.json   ← Product catalogue data (77 products — do not edit manually)
│   ├── images/
│   │   ├── icons/              ← Favicon files and web app icons
│   │   ├── gallery/            ← Home page images
│   │   └── products/           ← Product images, grouped by category
│   └── templates/
│       └── page-template.html  ← Copy this to start a new content page
│
├── layout/
│   ├── header.html             ← Shared site header (loaded by JavaScript)
│   └── footer.html             ← Shared site footer (loaded by JavaScript)
│
├── robots.txt
├── sitemap.xml
├── .htaccess                   ← Apache config for future host (does nothing on GitHub Pages)
├── assets/site.webmanifest     ← Web app manifest for browser icons
└── README.MD                   ← This file
```

---

## Run Locally

```bash
python -m http.server 8080
```

Then open **http://127.0.0.1:8080/**

> Use a proper local server (not `file://`) because the site uses `fetch()` to load the shared header and footer.

---

## Notes

- **`.htaccess`** is for the **future Apache/cPanel host only**. It does nothing on GitHub Pages.
  Read the comments inside it before enabling any redirects.
- **`assets/json/product_list.json`** is the product data source. Do not edit it by hand.
  All 77 product codes must stay exactly as they are.
- **`about/`** and **`contact/`** pages are placeholders. Add real content there when the client provides it.
- The shared header and footer (`layout/header.html`, `layout/footer.html`) are loaded by
  `loadComponents()` in `app.js`. The home page (`index.html`) has these inlined instead.

---

## How to Add a New Page

1. Copy `assets/templates/page-template.html` to the new location, e.g. `privacy/index.html`.
2. Update the `<title>`, `<meta name="description">`, and `<link rel="canonical">` in the `<head>`.
3. Update the Open Graph tags (`og:title`, `og:description`, `og:url`).
4. Write your page content inside the `<main>` section.
5. Add the new URL to `sitemap.xml`.
6. Add a link in `layout/footer.html` if needed.
7. Create a page-specific CSS file in `assets/css/` only if needed. Use only variables from `variables-theme.css`.

---

## Rename Note

The file is currently named `README.MD`. You can rename it to `README.md` (lowercase) with:

```bash
git mv README.MD README.md
git commit -m "chore: rename README to lowercase"
```
