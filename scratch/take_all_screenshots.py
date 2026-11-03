import subprocess
import os
import sys

out_dir = r'C:\Users\User\.gemini\antigravity\brain\a8b5bfad-ab49-4818-a85c-0de9ffc11a2c\scratch\screenshots'
os.makedirs(out_dir, exist_ok=True)
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

targets = [
    ('http://127.0.0.1:8080/products/index.html', 'products_desktop.png', 1280, 1600),
    ('http://127.0.0.1:8080/products/index.html', 'products_mobile.png', 390, 1400),
    ('http://127.0.0.1:8080/categories/sofa.html', 'category_sofa.png', 1280, 1600),
    ('http://127.0.0.1:8080/categories/mums.html', 'category_mums.png', 1280, 1400),
    ('http://127.0.0.1:8080/index.html', 'homepage_desktop.png', 1280, 1400)
]

for url, fname, w, h in targets:
    out_file = os.path.join(out_dir, fname)
    if os.path.exists(out_file) and os.path.getsize(out_file) > 10000:
        print(f'Already captured {fname} ({os.path.getsize(out_file)} bytes), skipping.', flush=True)
        continue

    cmd = [
        chrome,
        '--headless',
        '--disable-gpu',
        '--no-sandbox',
        f'--window-size={w},{h}',
        f'--screenshot={out_file}',
        url
    ]
    print(f'Capturing {url} -> {fname} ({w}x{h})...', flush=True)
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=35)
        if os.path.exists(out_file) and os.path.getsize(out_file) > 1000:
            print(f'  [SUCCESS] {fname} ({os.path.getsize(out_file)} bytes)', flush=True)
        else:
            print(f'  [FAILED] {fname}. Ret: {res.returncode}', flush=True)
    except Exception as e:
        print(f'  [ERROR] {fname}: {e}', flush=True)

print('All screenshots complete.', flush=True)
