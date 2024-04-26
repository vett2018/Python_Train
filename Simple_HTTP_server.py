from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        #self.wfile.write(b'Hello, world!')
        self.wfile.write(b'<html> '
                            b'<body>'
                                b'<br>Saint-Pitersburg is a great city</br>'
                                b'<br> <font color = "purple"> Saint-Pitersburg is a great city </font></br>'
                                b'<br> <font color = "green"> Saint-Pitersburg is a great city </font></br>'
                                b'<br><font color = "orange" size ="6"> Saint-Pitersburg is a great city </font></br>'
                                b'<table>'
                                    b'<tr>'
                                        b'<th> P/P </th>'
                                        b'<th> Country </th>'
                                        b'<th> City </th>'
                                        b'<th> Area </th>'
                                    b'</tr>'
                                    b'<tr>'
                                        b'<td> 1. </td>'
                                        b'<td> Brasil </td> <td> Rio-De-Ganerio </td><td>255 000 km</td>'
                                    b'</tr>'    
                                    b'<tr>'
                                        b'<td> 2. </td>'
                                        b'<td> Russia </td> <td>Moscow</td><td>500 000 km</td>'
                                    b'</tr>'
                            b'</body>'
                         b'</html>')
        self.wfile.write()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())


if __name__ == '__main__':

    httpd = HTTPServer(('192.168.0.100', 8000), SimpleHTTPRequestHandler)
    httpd.serve_forever()
