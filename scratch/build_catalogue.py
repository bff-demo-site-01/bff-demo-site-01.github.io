import os
import json
import re
from PIL import Image, ImageOps

# Ensure output directories exist
base_out = 'assets/images/products'
for cat in ['sofa', 'mate', 'screen', 'flower', 'bouquet', 'mums', 'carnation']:
    os.makedirs(os.path.join(base_out, cat), exist_ok=True)

def optimize_image(src_path, dest_path, max_dim=1000, quality=85):
    im = Image.open(src_path)
    # Correct orientation from EXIF
    im = ImageOps.exif_transpose(im)
    im = im.convert('RGB')
    im.thumbnail((max_dim, max_dim), Image.Resampling.LANCZOS)
    im.save(dest_path, 'JPEG', quality=quality, optimize=True)
    return dest_path

# 1. Sofa mappings
sofa_src = [
    ('MS_W1_001', 'Sofa White', 'WhatsApp Image 2026-03-18 at 2.34.01 PM.jpeg', 1),
    ('MS_YW_002', 'Sofa Yellow', 'WhatsApp Image 2026-03-18 at 2.34.02 PM.jpeg', 1),
    ('MS_GY_003', 'Sofa Grey', 'WhatsApp Image 2026-03-18 at 2.34.03 PM (1).jpeg', 1),
    ('MS_MN_004', 'Sofa Maroon', 'WhatsApp Image 2026-03-18 at 2.34.03 PM (2).jpeg', 1),
    ('MS_W2_005', 'Sofa White', 'WhatsApp Image 2026-03-18 at 2.34.03 PM.jpeg', 2),
    ('MS_RO_006', 'Sofa Rose', 'WhatsApp Image 2026-03-18 at 2.34.04 PM (1).jpeg', 2),
    ('MS_PH_007', 'Sofa Peach', 'WhatsApp Image 2026-03-18 at 2.34.04 PM (2).jpeg', 2),
    ('MS_W3_008', 'Sofa White', 'WhatsApp Image 2026-03-18 at 2.34.04 PM (3).jpeg', 2),
    ('MS_W4_009', 'Sofa White', 'WhatsApp Image 2026-03-18 at 2.34.04 PM.jpeg', 3),
    ('MS_RD_0010', 'Sofa Red', 'WhatsApp Image 2026-03-18 at 2.34.05 PM (1).jpeg', 3),
    ('MS_AB_011', 'Sofa Astriek Blue', 'WhatsApp Image 2026-03-18 at 2.34.05 PM (2).jpeg', 3),
    ('MS_W5_012', 'Sofa White', 'WhatsApp Image 2026-03-18 at 2.34.05 PM.jpeg', 3),
    ('MS_RD_013', 'Sofa Red', 'WhatsApp Image 2026-03-18 at 2.34.06 PM (1).jpeg', 4),
    ('MS_L1_014', 'Sofa Lavender', 'WhatsApp Image 2026-03-18 at 2.34.06 PM (2).jpeg', 4),
    ('MS_W6_015', 'Sofa White', 'WhatsApp Image 2026-03-18 at 2.34.06 PM.jpeg', 4),
    ('MS_PK_016', 'Sofa Pink', 'WhatsApp Image 2026-03-18 at 2.34.07 PM (1).jpeg', 4),
    ('MS_DG_017', 'Sofa Dark Green', 'WhatsApp Image 2026-03-18 at 2.34.07 PM (2).jpeg', 5),
    ('MS_L2_018', 'Sofa Lavender', 'WhatsApp Image 2026-03-18 at 2.34.07 PM (3).jpeg', 5),
    ('MS_BE_019', 'Sofa Blue', 'WhatsApp Image 2026-03-18 at 2.34.07 PM.jpeg', 5),
    ('MS_W7_020', 'Sofa White', 'WhatsApp Image 2026-03-18 at 2.34.08 PM (1).jpeg', 5),
    ('MS_L3_021', 'Sofa Lavender', 'WhatsApp Image 2026-03-18 at 2.34.08 PM (2).jpeg', 5),
    ('MS_W8_022', 'Sofa White', 'WhatsApp Image 2026-03-18 at 2.34.08 PM.jpeg', 6),
    ('MS_W9_023', 'Sofa White', 'WhatsApp Image 2026-03-18 at 2.34.09 PM.jpeg', 6)
]

# 2. Mate mappings
mate_src = [
    ('MM_GY_001', 'Mate 5223 Grey', 'WhatsApp Image 2026-02-04 at 11.41.06 AM (1).jpeg', 6),
    ('MM_CN_002', 'Mate 6574 Cyan', 'WhatsApp Image 2026-02-04 at 11.41.06 AM (2).jpeg', 6),
    ('MM_RW_003', 'Mate 5645 Rainbow', 'WhatsApp Image 2026-02-04 at 11.41.06 AM.jpeg', 6),
    ('MM_RD1_004', 'Mate 1261 Red', 'WhatsApp Image 2026-02-04 at 11.41.07 AM (1).jpeg', 7),
    ('MM_GD_005', 'Mate 1284 Gold', 'WhatsApp Image 2026-02-04 at 11.41.07 AM (2).jpeg', 7),
    ('MM_BN1_006', 'Mate 6541 Brown', 'WhatsApp Image 2026-02-04 at 11.41.07 AM.jpeg', 7),
    ('MM_CE_007', 'Mate 1111 Coffee', 'WhatsApp Image 2026-02-04 at 11.41.08 AM (1).jpeg', 7),
    ('MM_LT BN_008', 'Mate 3881 LT Brown', 'WhatsApp Image 2026-02-04 at 11.41.08 AM (2).jpeg', 7),
    ('MM_BE_009', 'Mate 5429 Beige', 'WhatsApp Image 2026-02-04 at 11.41.08 AM.jpeg', 8),
    ('MM_RD2_010', 'Mate 1633 Red', 'WhatsApp Image 2026-02-04 at 11.41.09 AM (1).jpeg', 8),
    ('MM_PE_011', 'Shubham Mate 2999 Purple', 'WhatsApp Image 2026-02-04 at 11.41.09 AM.jpeg', 8),
    ('MM_RD3_012', 'Mate 3399 Red', 'WhatsApp Image 2026-02-04 at 11.41.10 AM (1).jpeg', 8),
    ('MM_RD4_013', 'Shubham Mate 3500 Red', 'WhatsApp Image 2026-02-04 at 11.41.10 AM (2).jpeg', 8),
    ('MM_MN_014', 'Shubham Mate 1470 Maroon', 'WhatsApp Image 2026-02-04 at 11.41.10 AM (3).jpeg', 8),
    ('MM_BN2_015', 'Shubham Mate 353 Brown', 'WhatsApp Image 2026-02-04 at 11.41.11 AM (2).jpeg', 9),
    ('MM_RD5_016', 'Shubham Mate 1501 Red', 'WhatsApp Image 2026-02-04 at 11.41.11 AM (1).jpeg', 9)
]

# 3. Screen mappings
screen_src = [
    ('MS_W_001', 'Screen White', 'DSC05170.jpg.jpeg', 9),
    ('MS_G_002', 'Screen Green', 'DSC05172.jpg.jpeg', 9),
    ('MS_L_003', 'Screen Lavender', 'DSC05173.jpg.jpeg', 9),
    ('MS_R_004', 'Screen Red', 'DSC05175.jpg.jpeg', 10),
    ('MS_B_005', 'Screen Blue', 'DSC05176.jpg.jpeg', 10),
    ('MS_GR_006', 'Stall Screen Gold Red', 'PDF_EXTRACT:page_10_img_03.png', 10)
]

# 4. Flower mappings
flower_src = [
    ('MF_PR_001', 'Flower Pink Rose', 'Runner/DSC05114.jpg.jpeg', 10),
    ('MF_WR_002', 'Flower White Red', 'Runner/DSC05119.jpg.jpeg', 10),
    ('MF_R_003', 'Flower Red', 'Runner/DSC05123.jpg.jpeg', 10),
    ('MF_PH_004', 'Flower Peach', 'Hanging Flower set/DSC05127.jpg.jpeg', 11),
    ('MF_LR_005', 'Flower Lavender', 'Hanging Flower set/DSC05129.jpg.jpeg', 11),
    ('MF_WE_006', 'Flower White', 'Hanging Flower set/DSC05130.jpg.jpeg', 11),
    ('MF_BE_007', 'Flower Blue', 'Hanging Flower set/DSC05135.jpg.jpeg', 11),
    ('MF_RD_008', 'Flower Red', 'Hanging Flower set/DSC05137.jpg.jpeg', 11),
    ('MF_YW_009', 'Flower Yellow White', 'Runner/DSC05139.jpg.jpeg', 12),
    ('MF_W_010', 'Flower White', 'Runner/DSC05144.jpg.jpeg', 12),
    ('MF_WR_011', 'Flower White Red', 'Runner/DSC05148.jpg.jpeg', 12),
    ('MF_PWR1_012', 'Flower Pink White Red', 'Runner/DSC05150.jpg.jpeg', 12),
    ('MF_PWR2_013', 'Flower Pink White Red', 'Runner/DSC05155.jpg.jpeg', 12),
    ('MF_W_014', 'Flower White', 'Runner/DSC05157.jpg.jpeg', 13),
    ('MF_PK_015', 'Flower Pink', 'Hanging Flower set/DSC05159.jpg.jpeg', 13),
    ('MF_GN_016', 'Flower Green', 'Hanging Flower set/DSC05161.jpg.jpeg', 13)
]

# 5. Bouquet mappings
bouquet_src = [
    ('MF_BW_017', 'Bouquet White', 'Bowl/DSC05162.jpg.jpeg', 14),
    ('MF_BP_018', 'Bouquet Pink', 'Bowl/DSC05165.jpg.jpeg', 14),
    ('MF_BWR_019', 'Bouquet White Red', 'Bowl/DSC05166.jpg.jpeg', 14),
    ('MF_BWP_020', 'Bouquet White Pink', 'Bowl/DSC05168.jpg.jpeg', 15)
]

# 6. Mums (Group)
mums_src = [
    ('MM_PH_001', 'Mums Peach', 15),
    ('MM_PK_002', 'Mums Pink', 15),
    ('MM_WE_003', 'Mums White', 15),
    ('MM_YW_004', 'Mums Yellow', 15),
    ('MM_MN_005', 'Mums Maroon', 15),
    ('MM_LR_006', 'Mums Lavender', 15),
    ('MM_RD_007', 'Mums Red', 15)
]

# 7. Carnation (Group)
carnation_src = [
    ('MC_PK_001', 'Carnation Pink', 15),
    ('MC_YW_002', 'Carnation Yellow', 15),
    ('MC_LR_003', 'Carnation Lavender', 15),
    ('MC_WE_004', 'Carnation White', 15),
    ('MC_RD_005', 'Carnation Red', 15)
]

def make_code_slug(code):
    return re.sub(r'[^a-zA-Z0-9]+', '-', code.strip()).strip('-').lower()

# Generate web images for Sofa
products = []
display_order = 1

for code, name, fname, page in sofa_src:
    src_full = os.path.join('Google-Drive-Images/MSR-TentMart-Files/Sofa', fname)
    slug = make_code_slug(code)
    web_rel = f'assets/images/products/sofa/{slug}.jpg'
    optimize_image(src_full, web_rel)
    products.append({
        'id': f'sofa-{slug}',
        'code': code,
        'name': name,
        'categoryId': 'sofa',
        'displayOrder': display_order,
        'image': web_rel,
        'altText': f'{name} - Code: {code}',
        'price': None,
        'isGroupPhoto': False,
        'originalSource': f'Google-Drive-Images/MSR-TentMart-Files/Sofa/{fname}',
        'pdfPage': page
    })
    display_order += 1

# Generate web images for Mate
for code, name, fname, page in mate_src:
    src_full = os.path.join('Google-Drive-Images/MSR-TentMart-Files/Mate', fname)
    slug = make_code_slug(code)
    web_rel = f'assets/images/products/mate/{slug}.jpg'
    optimize_image(src_full, web_rel)
    products.append({
        'id': f'mate-{slug}',
        'code': code,
        'name': name,
        'categoryId': 'mate',
        'displayOrder': display_order,
        'image': web_rel,
        'altText': f'{name} - Code: {code}',
        'price': None,
        'isGroupPhoto': False,
        'originalSource': f'Google-Drive-Images/MSR-TentMart-Files/Mate/{fname}',
        'pdfPage': page
    })
    display_order += 1

# Generate web images for Screen
for code, name, fname, page in screen_src:
    slug = make_code_slug(code)
    web_rel = f'assets/images/products/screen/{slug}.jpg'
    if fname.startswith('PDF_EXTRACT:'):
        pdf_img_name = fname.split(':', 1)[1]
        src_full = os.path.join('C:/Users/User/.gemini/antigravity/brain/a8b5bfad-ab49-4818-a85c-0de9ffc11a2c/scratch/pdf_images', pdf_img_name)
        optimize_image(src_full, web_rel)
        orig_desc = 'PDF page 10 extracted image (client supplied)'
    else:
        src_full = os.path.join('Google-Drive-Images/MSR-TentMart-Files/Screen', fname)
        optimize_image(src_full, web_rel)
        orig_desc = f'Google-Drive-Images/MSR-TentMart-Files/Screen/{fname}'
    products.append({
        'id': f'screen-{slug}',
        'code': code,
        'name': name,
        'categoryId': 'screen',
        'displayOrder': display_order,
        'image': web_rel,
        'altText': f'{name} - Code: {code}',
        'price': None,
        'isGroupPhoto': False,
        'originalSource': orig_desc,
        'pdfPage': page
    })
    display_order += 1

# Generate web images for Flower
for code, name, rel_source, page in flower_src:
    src_full = os.path.join('Google-Drive-Images/MSR-TentMart-Files', rel_source)
    slug = make_code_slug(code)
    web_rel = f'assets/images/products/flower/{slug}.jpg'
    optimize_image(src_full, web_rel)
    products.append({
        'id': f'flower-{slug}',
        'code': code,
        'name': name,
        'categoryId': 'flower',
        'displayOrder': display_order,
        'image': web_rel,
        'altText': f'{name} - Code: {code}',
        'price': None,
        'isGroupPhoto': False,
        'originalSource': f'Google-Drive-Images/MSR-TentMart-Files/{rel_source}',
        'pdfPage': page
    })
    display_order += 1

# Generate web images for Bouquet
for code, name, rel_source, page in bouquet_src:
    src_full = os.path.join('Google-Drive-Images/MSR-TentMart-Files', rel_source)
    slug = make_code_slug(code)
    web_rel = f'assets/images/products/bouquet/{slug}.jpg'
    optimize_image(src_full, web_rel)
    products.append({
        'id': f'bouquet-{slug}',
        'code': code,
        'name': name,
        'categoryId': 'bouquet',
        'displayOrder': display_order,
        'image': web_rel,
        'altText': f'{name} - Code: {code}',
        'price': None,
        'isGroupPhoto': False,
        'originalSource': f'Google-Drive-Images/MSR-TentMart-Files/{rel_source}',
        'pdfPage': page
    })
    display_order += 1

# Optimize group images for Mums and Carnation
mums_group_web = 'assets/images/products/mums/mums-group.jpg'
optimize_image('assets/images/gallery/msr-tent-mart_big-mums.jpeg', mums_group_web)

carnation_group_web = 'assets/images/products/carnation/carnation-group.jpg'
optimize_image('assets/images/gallery/msr-tent-mart_carnation.jpeg', carnation_group_web)

# Mums products
for code, name, page in mums_src:
    slug = make_code_slug(code)
    products.append({
        'id': f'mums-{slug}',
        'code': code,
        'name': name,
        'categoryId': 'mums',
        'displayOrder': display_order,
        'image': None,
        'groupImage': mums_group_web,
        'isGroupPhoto': True,
        'altText': f'{name} (Code: {code}) - Color variant in Big Mums collection',
        'price': None,
        'originalSource': 'assets/images/gallery/msr-tent-mart_big-mums.jpeg (Group reference poster)',
        'pdfPage': page
    })
    display_order += 1

# Carnation products
for code, name, page in carnation_src:
    slug = make_code_slug(code)
    products.append({
        'id': f'carnation-{slug}',
        'code': code,
        'name': name,
        'categoryId': 'carnation',
        'displayOrder': display_order,
        'image': None,
        'groupImage': carnation_group_web,
        'isGroupPhoto': True,
        'altText': f'{name} (Code: {code}) - Color variant in Carnation collection',
        'price': None,
        'originalSource': 'assets/images/gallery/msr-tent-mart_carnation.jpeg (Group reference poster)',
        'pdfPage': page
    })
    display_order += 1

# Also create the legacy hero copies for index.html compatibility
legacy_hero_maps = [
    ('assets/images/products/sofa/ms-w1-001.jpg', 'assets/images/products/sofa-white-ms-w1-001.jpg'),
    ('assets/images/products/mate/mm-gy-001.jpg', 'assets/images/products/mate-5223-grey-mm-gy-001.jpg'),
    ('assets/images/products/screen/ms-w-001.jpg', 'assets/images/products/screen-white-ms-w-001.jpg'),
    ('assets/images/products/flower/mf-pr-001.jpg', 'assets/images/products/flower-pink-rose-mf-pr-001.jpg'),
    ('assets/images/products/bouquet/mf-bw-017.jpg', 'assets/images/products/bouquet-white-mf-bw-017.jpg'),
    (mums_group_web, 'assets/images/products/mums-peach-mm-ph-001.jpg'),
    (carnation_group_web, 'assets/images/products/carnation-pink-mc-pk-001.jpg')
]
for src, dest in legacy_hero_maps:
    optimize_image(src, dest)

categories = [
    {
        'id': 'sofa',
        'name': 'Sofa',
        'displayOrder': 1,
        'description': 'Exquisite range of premium sofa sets designed for elegant seating arrangements in weddings, corporate events, and special occasions.',
        'icon': 'fas fa-couch',
        'pageUrl': 'categories/sofa.html',
        'heroImage': 'assets/images/products/sofa/ms-w1-001.jpg',
        'productCount': len(sofa_src)
    },
    {
        'id': 'mate',
        'name': 'Mate',
        'displayOrder': 2,
        'description': 'Traditional and modern mate collections for cultural celebrations and wedding seating.',
        'icon': 'fas fa-chair',
        'pageUrl': 'categories/mate.html',
        'heroImage': 'assets/images/products/mate/mm-gy-001.jpg',
        'productCount': len(mate_src)
    },
    {
        'id': 'screen',
        'name': 'Screen',
        'displayOrder': 3,
        'description': 'Decorative stage screens and elegant stall backdrops for privacy, stages, and ambiance.',
        'icon': 'fas fa-columns',
        'pageUrl': 'categories/screen.html',
        'heroImage': 'assets/images/products/screen/ms-w-001.jpg',
        'productCount': len(screen_src)
    },
    {
        'id': 'flower',
        'name': 'Flower',
        'displayOrder': 4,
        'description': 'Beautiful floral runners, hanging flower sets, and decorative floral arrangements.',
        'icon': 'fas fa-flower',
        'pageUrl': 'categories/flower.html',
        'heroImage': 'assets/images/products/flower/mf-pr-001.jpg',
        'productCount': len(flower_src)
    },
    {
        'id': 'bouquet',
        'name': 'Bouquet',
        'displayOrder': 5,
        'description': 'Stunning floral bouquets and bowl centerpieces crafted for memorable events.',
        'icon': 'fas fa-seedling',
        'pageUrl': 'categories/bouquet.html',
        'heroImage': 'assets/images/products/bouquet/mf-bw-017.jpg',
        'productCount': len(bouquet_src)
    },
    {
        'id': 'mums',
        'name': 'Mums',
        'displayOrder': 6,
        'description': 'Chrysanthemum flower collections in diverse shades for vibrant festive decor.',
        'icon': 'fas fa-spa',
        'pageUrl': 'categories/mums.html',
        'heroImage': 'assets/images/products/mums/mums-group.jpg',
        'groupImage': mums_group_web,
        'hasGroupReferenceOnly': True,
        'productCount': len(mums_src)
    },
    {
        'id': 'carnation',
        'name': 'Carnation',
        'displayOrder': 7,
        'description': 'Classic carnation collections in vibrant shades for elegant celebrations.',
        'icon': 'fas fa-leaf',
        'pageUrl': 'categories/carnation.html',
        'heroImage': 'assets/images/products/carnation/carnation-group.jpg',
        'groupImage': carnation_group_web,
        'hasGroupReferenceOnly': True,
        'productCount': len(carnation_src)
    }
]

catalogue = {
    'meta': {
        'version': '2.0.0',
        'lastUpdated': '2026-11-04',
        'productCount': len(products),
        'categoryCount': len(categories),
        'pdfSource': 'Product List-Code - v001.pdf'
    },
    'config': {
        'whatsappNumber': '',
        'whatsappCandidateNumbers': ['6384500051', '8838318549'],
        'whatsappStatus': 'UNCONFIRMED_DESTINATION',
        'whatsappEnabled': False,
        'currencySymbol': '₹',
        'missingPriceLabel': 'Price on Request'
    },
    'categories': categories,
    'products': products
}

with open('assets/json/product_list.json', 'w', encoding='utf-8') as f:
    json.dump(catalogue, f, indent=2)

print(f'Successfully built catalogue with {len(products)} products and {len(categories)} categories.')

