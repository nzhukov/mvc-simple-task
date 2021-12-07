


from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        import models 
        import views.client as client_view


        # from jinja2 import Environment, PackageLoader, select_autoescape
        # env = Environment(
        #     loader=PackageLoader('app', 'templates'),
        #     autoescape=select_autoescape(['html', 'xml']))

        self.send_response(200)
        # self.send_header('Content-type', 'text/html')
        self.send_header('Content-Type', 'text/html, charset="utf-8"')
        self.end_headers()

        c = models.client.Client('Коля', 'Жуков', None, None, None, None) 


        result = client_view.render_client(c)

        result = bytes(result, 'utf-8')

        self.wfile.write(result)

        # '<html>Hello, Nick!</html>'

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html, charset="utf-8"')
        self.end_headers()

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        # действия по считыванию данных
        result = f'<html><head><title>OK. Data got.</title><meta charset="utf-8"></head><body>Данные получены: {(body)} </body></html>'
        result = bytes(result,'utf-8')

        self.wfile.write(result)



httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()