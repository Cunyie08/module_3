from http.server import BaseHTTPRequestHandler, HTTPServer
import json

data = [
        {
            'name': 'Kayla John',
            'track': 'AI Developer'
        }
]

class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, data, status=201):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json') # Mapping
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_DELETE(self):
        self.send_data(data)

def run():
    HTTPServer(('localhost', 8000), BasicAPI).serve_forever()


print('Application is running')
run()