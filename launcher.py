import http.server
import socketserver
import webbrowser
import threading
import os
import sys
import time

PORT = 8765

# Find the bundled HTML folder whether running as .py or .exe
if getattr(sys, 'frozen', False):
    base_dir = sys._MEIPASS
else:
    base_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(base_dir)

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

def start_server():
    with socketserver.TCPServer(("127.0.0.1", PORT), QuietHandler) as httpd:
        httpd.serve_forever()

threading.Thread(target=start_server, daemon=True).start()
time.sleep(0.5)
webbrowser.open(f"http://127.0.0.1:{PORT}/index.html")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    sys.exit(0)
