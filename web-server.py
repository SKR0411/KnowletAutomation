from http.server import SimpleHTTPRequestHandler, HTTPServer
import os
import socket

class HtmlFallbackHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, directory=None, **kwargs):
        self.directory = directory
        super().__init__(*args, directory=directory, **kwargs)

    def do_GET(self):
        path = self.path.split("?")[0]

        # If no file extension, try .html fallback
        if not os.path.splitext(path)[1]:
            html_path = path.rstrip("/") + ".html"
            full_path = os.path.join(self.directory, html_path.lstrip("/"))
            if os.path.exists(full_path):
                self.path = html_path

        super().do_GET()


def get_local_ip():
    """Gets the local network IP (Wi-Fi / Hotspot)"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip


# ===== Ask for project path =====

webPath = "/sdcard/.workspace/web"
project_path = webPath + input("Enter project folder path to host: " + webPath).strip()

if not os.path.isdir(project_path):
    print("❌ Invalid directory path")
    exit(1)

project_path = os.path.abspath(project_path)

PORT = 5000
HOST = "0.0.0.0"

handler = lambda *args, **kwargs: HtmlFallbackHandler(
    *args,
    directory=project_path,
    **kwargs
)

server = HTTPServer((HOST, PORT), handler)

local_ip = get_local_ip()

print("\nServer running:")
print(f"• Localhost : http://127.0.0.1:{PORT}")
print(f"• Network   : http://{local_ip}:{PORT}")
print(f"• Hosting   : {project_path}")
print("\nOpen the Network URL on devices connected to the same Wi-Fi or hotspot.\n")

server.serve_forever()