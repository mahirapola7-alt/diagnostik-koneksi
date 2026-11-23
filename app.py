"""Public connectivity diagnostic; no voucher or account processing."""
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class Handler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

    def reply(self, status, data):
        body = json.dumps(data).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Cache-Control', 'no-store')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path in ('/', '/health'):
            self.reply(200, {'status': 'diagnostic_only', 'claims_enabled': False})
        else:
            self.reply(404, {'error': 'not_found'})

    def do_POST(self):
        self.close_connection = True
        self.reply(403, {'error': 'claims_not_available'})


if __name__ == '__main__':
    ThreadingHTTPServer(('0.0.0.0', int(os.environ.get('PORT', '10000'))), Handler).serve_forever()
