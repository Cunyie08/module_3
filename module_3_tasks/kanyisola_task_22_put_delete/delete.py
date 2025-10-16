from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# View the data
data = [
    {
    "Name": "Vanessa Bryant",
    "Track": "Brand influencer",
    "Age": 45
    },

    {
    "Name": "Bryan Jordan",
    "Track": "Movie Producer",
    "Age": 35
    }
    ]

class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, payload, status=201):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())

    
    def do_DELETE(self):
        if data:
            data.clear()
            self.send_data({
            "Message": "Data deleted successfully!",
            "data": []
            })
        else:
            self.send_data({
            "Message": "There is no data to delete!"
            })

def run():
    HTTPServer(("localhost", 5000), BasicAPI).serve_forever()

print("Application running successfully")
run()
