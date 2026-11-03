import subprocess
import os
import sys

out_dir = r'C:\Users\User\.gemini\antigravity\brain\a8b5bfad-ab49-4818-a85c-0de9ffc11a2c\scratch\screenshots'
os.makedirs(out_dir, exist_ok=True)
user_data = r'C:\Users\User\.gemini\antigravity\brain\a8b5bfad-ab49-4818-a85c-0de9ffc11a2c\scratch\chrome_data_test'
os.makedirs(user_data, exist_ok=True)

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

url = sys.argv[1] if len(sys.argv) > 1 else 'http://127.0.0.1:8080/products/index.html'
out_file = sys.argv[2] if len(sys.argv) > 2 else os.path.join(out_dir, 'products_desktop.png')
width = int(sys.argv[3]) if len(sys.argv) > 3 else 1280
height = int(sys.argv[4]) if len(sys.argv) > 4 else 900

cmd = [
    chrome,
    '--headless=new',
    '--disable-gpu',
    '--no-sandbox',
    '--disable-extensions',
    '--disable-sync',
    f'--user-data-dir={user_data}',
    f'--window-size={width},{height}',
    '--virtual-time-budget=2500',
    f'--screenshot={out_file}',
    url
]

print(f'Capturing {url} -> {out_file} ({width}x{height})...', flush=True)
res = subprocess.run(cmd, capture_output=True, text=True, timeout=12)
print('Exit code:', res.returncode, flush=True)
if os.path.exists(out_file):
    print(f'SUCCESS: {out_file} created ({os.path.getsize(out_file)} bytes)', flush=True)
else:
    print(f'FAILED to create screenshot. Stderr: {res.stderr}', flush=True)

