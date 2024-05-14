from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 8000

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)

        self.send_header('Content-type','text/html')
        self.end_headers()
        
        self.wfile.write(b"<html><head><title>Student</title></head>")
        self.wfile.write(b"<body><h1>Student Info</h1>")
        self.wfile.write(b"<form>")
        self.wfile.write(b"<div>Ime: Ivana</div>")
        self.wfile.write(b"<div>Prezime: Matic</div>")
        self.wfile.write(b"<div>Datum: 14/05/2024</div>")
        self.wfile.write(b"</form>")
        self.wfile.write(b"</body></html>")
        return


try:
    server = HTTPServer(('', PORT), Handler)
    print('Started http server on port ', PORT)
    
    server.serve_forever()

except KeyboardInterrupt:
    print('^C received, exiting and shutting down the web server!')
    server.socket.close()
