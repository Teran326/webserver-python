from http.server import HTTPServer, BaseHTTPRequestHandler



class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write("Hello world!".encode())

def main():
        PORT = 8000
        server = HTTPServer(('', PORT), handler)
        print("Server running on port %s" % PORT)
        server.serve_forever()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

