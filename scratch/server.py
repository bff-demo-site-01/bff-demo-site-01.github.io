from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import sys

class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

server = ThreadingHTTPServer(('127.0.0.1', 8080), Handler)
print('Multi-threaded HTTP Server running on http://127.0.0.1:8080', flush=True)
server.serve_forever()

