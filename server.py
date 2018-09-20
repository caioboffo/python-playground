import http.server
import socketserver

port = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", port), Handler) as httpd:
    print("serving at port", port)
    httpd.serve_forever()
