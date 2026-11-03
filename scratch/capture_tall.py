import subprocess
import os

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
out_file = r'C:\Users\User\.gemini\antigravity\brain\a8b5bfad-ab49-4818-a85c-0de9ffc11a2c\scratch\screenshots\products_grid_desktop.png'

# We can run headless with 1280x3200 to capture the whole page down to footer
cmd = [
    chrome,
    '--headless',
    '--disable-gpu',
    '--no-sandbox',
    '--window-size=1280,3200',
    f'--screenshot={out_file}',
    'http://127.0.0.1:8080/products/index.html'
]
subprocess.run(cmd, capture_output=True, text=True, timeout=35)
print('Done. Size:', os.path.getsize(out_file) if os.path.exists(out_file) else 0)

