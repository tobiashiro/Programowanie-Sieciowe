import http.server
import socketserver
import re


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):

    def get_content(self, numer_of_page: int):
        if 1 <= int(numer_of_page) <= 5:
            numer_of_page = str(numer_of_page) + ".txt"
            with open(numer_of_page, 'r') as file:
                data = file.read().replace('\n', '')
            return data
        else:
            return "Magazyn nie istnieje lub wpisales blednie magazyn! Wpisz np. http://localhost:5555/1"

    def get_sum(self, content):
        sum_of_price = 0
        pattern = "<td>[0-9]+</td>"
        result = re.findall(pattern, content)
        for i in result:
            value = i.strip("<>/td")
            sum_of_price = sum_of_price + int(value)
        return sum_of_price

    def do_GET(self):
        html = ""
        list_of_pages = []
        # Sending an '200 OK' response
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        for i in self.path:
            if i.isnumeric():
                list_of_pages.append(i)

        for page in list_of_pages:
            html = html + self.get_content(page)

        if "http://localhost:5555/1" in html:
            html = "Magazyn nie istnieje lub wpisales blednie magazyn! Wpisz np. http://localhost:5555/1"

        html = "<table border= '1' >" + html + "</table> </br> </br> <table border= '1' > <tr> " \
                                                            "<td>suma </td> <td>{}</td> </tr>".format(self.get_sum(html))

        self.wfile.write(bytes(html, "utf8"))
        return



handler_object = MyHttpRequestHandler

PORT = 5555
print("start listening on http://localhost:5555/")
my_server = socketserver.TCPServer(("", PORT), handler_object)
my_server.serve_forever()