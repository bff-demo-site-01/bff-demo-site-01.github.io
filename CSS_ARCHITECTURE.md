
# MSR Tent Mart - CSS Architecture Guide

## 📋 Overview

The CSS has been organized into a modular, reusable structure to maintain consistency across all pages while keeping pages lightweight and maintainable.

## 📁 CSS File Structure

```
assets/css/
├── variables-theme.css    # Color palette, typography, spacing, shadows
├── globals.css            # Animations, utilities, global elements
└── index.css             # Page-specific styles for homepage
```

## 📚 File Descriptions

### 1. **variables-theme.css**
**Purpose:** Brand identity and reusable variables
- Color variables (primary, accent, backgrounds, text, borders)
- Typography variables (font sizes, weights)
- Spacing scale (margins, padding)
- Border radius values
- Shadow utilities
- Z-index management
- Transition timings

**Use in new pages:**
```css
@import url('variables-theme.css');
```

**Example usage of variables:**
```css
.my-element {
    color: var(--primary-color);
    background-color: var(--background-light);
    padding: var(--space-4);
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-lg);
}
```

---

### 2. **globals.css**
**Purpose:** Reusable animations, utilities, and base styles
- **Animations:** fadeIn, fadeOut, slideInUp, slideInDown, slideInLeft, slideInRight, scaleIn, pulse
- **Animation Utilities:** `.animate-fade-in`, `.animate-slide-up`, etc.
- **Typography Utilities:** Text colors, sizes, weights, alignment
- **Background Utilities:** Color classes
- **Spacing Utilities:** Margin, padding, gap classes
- **Display Utilities:** Flex, grid, display classes
- **Hover States:** Interactive element states
- **Glass Effect:** Frosted glass styling

**Common Animation Classes:**
```html
<div class="animate-fade-in">Fades in on page load</div>
<div class="animate-slide-up animation-delay-200">Slides up with 200ms delay</div>
<div class="animate-scale-in">Scales in smoothly</div>
```

**Spacing Utilities Example:**
```html
<div class="m-4 p-6 gap-8">Margin, padding, gap all applied</div>
```

---

### 3. **index.css**
**Purpose:** Homepage-specific styling
- Header and navigation styles
- Hero section styles
- Service cards styling
- Gallery grid layout
- Contact form styling
- Footer layout
- All section-specific animations

---

## 🎨 How to Create New Pages

### Step 1: Create a New Page HTML File
Example: `about-us.html` or `services.html`

### Step 2: Create a New CSS File
Example: `assets/css/about.css` or `assets/css/services.css`

### Step 3: Link CSS Files in Your HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- ... other meta tags ... -->
    
    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    
    <!-- Google Fonts & Material Icons -->
    <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght@100..700,0..1&display=swap" rel="stylesheet">
    
    <!-- MSR Tent Mart Custom Stylesheets (Shared) -->
    <link href="assets/css/variables-theme.css" rel="stylesheet">
    <link href="assets/css/globals.css" rel="stylesheet">
    
    <!-- Page-Specific CSS (New) -->
    <link href="assets/css/about.css" rel="stylesheet">
</head>
<body>
    <!-- ... your content ... -->
</body>
</html>
```

### Step 4: Use Variables in New CSS File
```css
/* about.css - Page-specific styles */

/* About section with brand colors from variables */
.about-hero {
    background-color: var(--background-light);
    color: var(--text-light);
    padding: var(--space-24);
}

/* Use animations from globals */
.about-card {
    animation: slideInUp var(--transition-base) ease-out;
}

/* Use spacing utilities */
.about-grid {
    gap: var(--gap-6);
    padding: var(--space-8);
}

/* Use brand colors for links */
.about-link {
    color: var(--primary-color);
    transition: color var(--transition-base);
}

.about-link:hover {
    color: var(--accent-gold);
}
```

---

## 🎭 Color System

### Primary Colors
```css
--primary-color: #800000        /* Maroon - Main brand color */
--accent-gold: #C5A059         /* Gold - Accent color */
```

### Background Colors
```css
--background-light: #f8f5f5    /* Light theme background */
--background-dark: #230f0f     /* Dark theme background */
```

### Text Colors
```css
--text-light: #1f2937          /* Primary text on light backgrounds */
--text-dark: #f3f4f6           /* Primary text on dark backgrounds */
--text-muted-light: #6b7280    /* Secondary text on light backgrounds */
--text-muted-medium: #9ca3af   /* Secondary text on dark backgrounds */
```

---

## ✨ Animation Examples

### Fade In Animation
```html
<section class="animate-fade-in">
    This section fades in on page load
</section>
```

### Staggered Animations
```html
<div class="animate-slide-up animation-delay-100">Item 1</div>
<div class="animate-slide-up animation-delay-200">Item 2</div>
<div class="animate-slide-up animation-delay-300">Item 3</div>
```

### Scale Animation
```html
<div class="animate-scale-in">Scales in smoothly</div>
```

### Pulse Animation
```html
<div class="animate-pulse">Pulsing element</div>
```

---

## 🔧 Utility Classes (Pre-built)

### Text Utilities
```html
<p class="text-primary">Primary color text</p>
<p class="text-accent-gold">Accent gold text</p>
<p class="text-2xl font-bold">Large bold text</p>
<p class="text-center uppercase">Centered uppercase</p>
<p class="tracking-widest">Wide letter spacing</p>
```

### Spacing Utilities
```html
<div class="m-4">Margin: 1rem all sides</div>
<div class="p-8">Padding: 2rem all sides</div>
<div class="mt-6">Margin-top: 1.5rem</div>
<div class="px-4">Padding: left & right 1rem</div>
<div class="gap-6">Gap between flex/grid items: 1.5rem</div>
```

### Shadow Utilities
```html
<div class="shadow-md">Medium shadow</div>
<div class="shadow-lg">Large shadow</div>
<div class="shadow-xl">Extra large shadow</div>
```

### Display Utilities
```html
<div class="d-flex justify-center items-center gap-4">
    Flexbox centered with gap
</div>
```

### Responsive Classes
```html
<div class="px-responsive">
    Responsive padding (1rem mobile, 1.5rem tablet, 2rem desktop)
</div>
```

---

## 🌙 Dark Mode Support

All CSS variables support dark mode automatically through the dark mode prefix:

```css
body.dark-mode {
    --background-light: var(--background-dark);
    --text-light: var(--text-dark);
}
```

Use in your CSS:
```css
.my-element {
    background-color: var(--background-light);
    color: var(--text-light);
}

body.dark-mode .my-element {
    background-color: var(--background-dark);
    color: var(--text-dark);
}
```

---

## 📱 Responsive Breakpoints

Bootstrap breakpoints are available:
- **xs:** 0px (mobile)
- **sm:** 576px (landscape mobile)
- **md:** 768px (tablet)
- **lg:** 992px (desktop)
- **xl:** 1200px (large desktop)
- **xxl:** 1400px (extra large)

Example:
```css
@media (min-width: 768px) {
    .my-element {
        font-size: 2rem;
    }
}
```

---

## 📝 Best Practices

1. **Use Variables:** Always use CSS variables instead of hardcoding colors/spacing
   ```css
   ✅ background-color: var(--primary-color);
   ❌ background-color: #800000;
   ```

2. **Organize by Purpose:** Keep page-specific styles in page-specific CSS files

3. **Reuse Animations:** Use predefined animation classes from globals.css
   ```html
   ✅ <div class="animate-fade-in">
   ❌ <div style="animation: fadeIn 0.3s ease-out;">
   ```

4. **Use Semantic Classes:** Use meaningful class names
   ```css
   ✅ .service-card-title
   ❌ .title1, .t
   ```

5. **Combine Utilities:** Mix utility and custom classes for flexibility
   ```html
   <div class="gap-4 my-8 animate-slide-up">
       Combines multiple utilities and animations
   </div>
   ```

---

## 🔄 File Size Optimization

Current file sizes:
- `variables-theme.css` ~ 2KB (shared across all pages)
- `globals.css` ~ 8KB (shared across all pages)
- `index.css` ~ 6KB (page-specific)

**Total for homepage:** ~16KB (dramatically reduced from original inline styles)

Each new page only needs to load:
- `variables-theme.css` (cached from index)
- `globals.css` (cached from index)
- `page-specific.css` (typically 3-5KB)

---

## 🚀 Quick Start for New Pages

1. Copy this template:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Title | MSR Tent Mart</title>
    
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght@100..700,0..1&display=swap" rel="stylesheet">
    
    <link href="assets/css/variables-theme.css" rel="stylesheet">
    <link href="assets/css/globals.css" rel="stylesheet">
    <link href="assets/css/page-name.css" rel="stylesheet">
</head>
<body>
    <!-- Header and footer can be shared/included -->
    <header><!-- ... --></header>
    <main><!-- Your content --></main>
    <footer><!-- ... --></footer>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

2. Create `assets/css/page-name.css` with page-specific styles
3. Use variables and utility classes from `globals.css`
4. Reference variables from `variables-theme.css` for colors and spacing

---

## 📞 Questions?

Refer to:
- Variable names in `variables-theme.css`
- Available utilities in `globals.css`
- Animation names and classes in `globals.css`
