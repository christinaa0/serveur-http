from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json
from models import Game

game = Game(nb_max_turn=50, width=10, height=10)

class SimpleGameServer(BaseHTTPRequestHandler):

    def _send_response(self, status=200, body=None):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        if body is not None:
            self.wfile.write(json.dumps(body).encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)

        if self.path == "/players":
            self._send_response(400, {"error": "players route removed"})
            return
        elif self.path == "/action":
            self._send_response(400, {"error": "action route removed"})
            return

    def do_GET(self):
        parsed_url = urlparse(self.path)
        if parsed_url.path == "/state":
            query_params = parse_qs(parsed_url.query)
            pseudo = query_params.get("pseudo", [None])[0]
            board = game._Game__gameboard.to_list()
            self._send_response(200, {"board": board, "pseudo": pseudo})
        else:
            self._send_response(404, {"error": "Not found"})

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleGameServer)
    print(f"Serveur HTTP démarré sur le port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()


#sa_model alexendre ou Christophe / gprcp thomas