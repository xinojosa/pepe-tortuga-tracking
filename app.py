cat << 'EOF' > app.py
from http.server import HTTPServer, BaseHTTPRequestHandler

class TrackingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        html = """
        <html>
            <head><title>Transportes Pepe Tortuga S.A.</title></head>
            <body style="font-family: Arial; text-align: center; margin-top: 50px;">
                <h1>🚛 Transportes Pepe Tortuga S.A.</h1>
                <h2>Panel de Rastreo de Flotas en Tiempo Real</h2>
                <p><strong>Estado del servicio:</strong> Operativo 🟢</p>
                <p><strong>Camiones monitoreados:</strong> 12 unidades activas.</p>
            </body>
        </html>
        """
        self.wfile.write(html.encode('utf-8'))

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 5000), TrackingHandler)
    print("Servidor de rastreo escuchando en el puerto 5000...")
    server.serve_forever()
EOF
