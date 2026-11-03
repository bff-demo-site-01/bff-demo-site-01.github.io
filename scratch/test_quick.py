import subprocess
import os
import time

out = os.path.abspath('scratch/quick.png')
t0 = time.time()
cmd = [
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    '--headless',
    '--disable-gpu',
    '--no-sandbox',
    '--disable-background-networking',
    '--disable-component-update',
    '--disable-default-apps',
    '--disable-sync',
    '--metrics-recording-only',
    '--window-size=1280,1600',
    f'--screenshot={out}',
    'http://127.0.0.1:8080/products/index.html'
]
res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
dur = time.time() - t0
print(f'Done in {dur:.1f}s. Exists: {os.path.exists(out)}, size: {os.path.getsize(out) if os.path.exists(out) else 0}')

