import http.server
import socketserver
import json

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """HTTP GET müraciətlərini idarə edən sinif"""

    def do_GET(self):
        # 1. Ana səhifə (/)
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # 2. /data (JSON)
        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))

        # 3. /status (OK)
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # 4. /info (Tapşırıq tələbi)
        elif self.path == '/info':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode('utf-8'))

        # 5. Tapılmayan endpoint-lər (404 Error)
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            # Mesajı tapşırıqdakı "Endpoint not found" ilə əvəz etdik
            self.wfile.write(b"Endpoint not found")

if __name__ == "__main__":
    PORT = 8000
    # Adətən bu tapşırıqlarda 'allow_reuse_address' istifadə olunmalıdır ki, error verməsin
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), SimpleAPIHandler) as httpd:
        print(f"Server {PORT} portunda işləyir...")
        httpd.serve_forever()
