from http.server import BaseHTTPRequestHandler, HTTPServer
import json

data =   [
        {
        "name": "Kayla John",
        "track": "AI Developer"
        },

        {
        "name": "Blessing James",
        "track": "Cyber Security"
        }
      
        ]

class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, payload, status=201): # serving as the response
        self.send_response(status)
        self.send_header('Content-Type', 'application/json') # Mapping
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())

    def do_PUT(self):
        content_size = int(self.headers.get('Content-Length', 0))
        parsed_data = self.rfile.read(content_size)

        put_data = json.loads(parsed_data)
        
        if data:
            data[0] = put_data 
            self.send_data({
            'Message': 'Data Replaced',
            'data': data[0]
            })
        else:
            data.append(put_data)
            self.send_data({
            'Message': "Data added successfully!",
            'data': put_data
            })


def run():
    HTTPServer(('localhost', 5000), BasicAPI).serve_forever()


print('Application is running')
run()