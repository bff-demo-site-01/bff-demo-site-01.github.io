import json
import os

with open('assets/json/product_list.json', 'r', encoding='utf-8') as f:
    catalogue = json.load(f)

products = catalogue['products']
categories = catalogue['categories']

report_path = r'C:\Users\User\.gemini\antigravity\brain\a8b5bfad-ab49-4818-a85c-0de9ffc11a2c\catalogue_reconciliation_report.md'

table_rows = []
for p in products:
    page = p.get('pdfPage', '-')
    code = p.get('code', '-')
    name = p.get('name', '-')
    cat = p.get('categoryId', '-')
    src = p.get('originalSource', '-')
    img = p.get('image') or p.get('groupImage', '-')
    is_grp = 'Yes (Palette Swatch)' if p.get('isGroupPhoto') else 'No (Direct 1:1)'
    table_rows.append(f"| {page} | `{code}` | {name} | `{cat}` | `{src}` | `{img}` | {is_grp} |")

mapping_table = "\n".join(table_rows)

print(f"Generated {len(table_rows)} table rows.")
with open('scratch/mapping_table.txt', 'w', encoding='utf-8') as f:
    f.write(mapping_table)

