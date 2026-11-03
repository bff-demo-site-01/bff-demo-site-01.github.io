with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add catalogue.css
if 'assets/css/catalogue.css' not in content:
    content = content.replace('<link href="assets/css/index.css" rel="stylesheet">',
                              '<link href="assets/css/index.css" rel="stylesheet">\n    <link href="assets/css/catalogue.css" rel="stylesheet">')

# 2. Fix our-products.html
content = content.replace('<li><a href="our-products.html">Our Products</a></li>',
                          '<li><a href="products/index.html">Our Products</a></li>')

# 3. Add await initHomePage();
old_init = 'await loadComponents();'
new_init = 'await loadComponents();\n            await initHomePage();'
if 'initHomePage()' not in content:
    content = content.replace(old_init, new_init, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated index.html successfully.')

