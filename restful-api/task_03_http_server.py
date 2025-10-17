#!/usr/bin/python3
"""
This module provides a simple HTTP server.
"""

import http.server
import json


class Handler(http.server.BaseHTTPRequestHandler):
    """
    defines Handler.
    """
    def do_GET(self):
        """
        automatically called whenever server receives a GET request
        receives and responds to GET requests
        """
        # root path response
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # /data endpoint response
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            j = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(j).encode())

        # /status endpoint response
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')

        # /info endpoint response
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            j = {"version": "1.0", "description":
                 "A simple API built with http.server"}
            self.wfile.write(json.dumps(j).encode())

        # error handling
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def start_server():
    """
    start server on port 8000
    """
    # create the server address (listen on all netwrok interfaces, port 8000)
    server_address = ('', 8000)
    # create new HTTP server instance
    h = http.server.HTTPServer(server_address, Handler)
    print('server started')
    # ensure server keeps running and listening for requests
    h.serve_forever()

start_server()
