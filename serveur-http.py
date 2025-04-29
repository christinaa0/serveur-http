from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from models import Game

game = Game(nb_max_turn=50, width=10, height=10)

paths = {
    '/players': 'add_player',
    '/action': 'process_action',
    '/state': 'get_state'
}

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
        if self.path == "/state":
            self.get_state()

    def get_state(self):
        board = repr(game._Game__gameboard)
        self._send_response(200, {"board": board})

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleGameServer)
    print(f"Serveur HTTP démarré sur le port {port}")
    httpd.serve_forever()


if __name__ == '__main__':
    run_server()
