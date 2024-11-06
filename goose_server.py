import http.server
import socketserver
import urllib.parse
import subprocess

PORT = 7788

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_path.query)
        
        if 'on' in query_params:
            try:
                subprocess.run(["./GooseDesktop.exe"], check=True)
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"GooseDesktop.exe executed successfully")
            except subprocess.CalledProcessError:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b"Failed to execute GooseDesktop.exe")
        
        elif 'off' in query_params:
            try:
                subprocess.run(["./CloseGoose.bat"], check=True)
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"CloseGoose.bat executed successfully")
            except subprocess.CalledProcessError:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b"Failed to execute CloseGoose.bat")
        
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid request")

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()