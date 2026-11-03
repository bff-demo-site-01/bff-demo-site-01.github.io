with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('<script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script>', '')
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Removed cloudflare script from index.html')

