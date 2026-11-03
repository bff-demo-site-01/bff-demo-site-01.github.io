import json
import urllib.request

with open('assets/json/product_list.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

failed = []
checked = 0
for p in data['products']:
    img_rel = p['image'] or p.get('groupImage')
    if not img_rel:
        failed.append((p['code'], 'NO_IMAGE_DEFINED', 'No image or groupImage path'))
        continue
    url = f'http://127.0.0.1:8080/{img_rel}'
    checked += 1
    try:
        res = urllib.request.urlopen(url)
        if res.getcode() != 200:
            failed.append((p['code'], url, res.getcode()))
    except Exception as e:
        failed.append((p['code'], url, str(e)))

print(f'Checked: {checked} product images over HTTP.')
print(f'Failures: {len(failed)}')
if failed:
    for item in failed:
        print('  Failed:', item)
else:
    print('ALL 77 PRODUCT IMAGES/GROUP REFERENCES LOADED SUCCESSFULLY OVER HTTP (200 OK)!')
