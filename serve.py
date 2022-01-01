import os
from http.server import HTTPServer, CGIHTTPRequestHandler

print('http://localhost:876')
os.chdir('.')
server_object = HTTPServer(server_address=('', 876), RequestHandlerClass=CGIHTTPRequestHandler)
server_object.serve_forever()
