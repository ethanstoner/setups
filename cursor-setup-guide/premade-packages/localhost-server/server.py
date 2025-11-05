#!/usr/bin/env python3
"""
Localhost HTTP Server
A simple HTTP server with auto-browser opening and error handling.
"""

import http.server
import socketserver
import webbrowser
import threading
import os
import sys
import argparse

def start_localhost_server(port=5173, directory=None, open_browser=True):
    """
    Start a simple HTTP server on localhost.
    
    Args:
        port (int): Port number (default: 5173)
        directory (str, optional): Directory to serve. Defaults to current directory.
        open_browser (bool): Whether to open browser automatically
    """
    if directory:
        if not os.path.exists(directory):
            print(f"Error: Directory '{directory}' does not exist")
            sys.exit(1)
        os.chdir(directory)
    
    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), handler)
    
    server_url = f"http://localhost:{port}"
    
    print(f"Server starting on {server_url}")
    print(f"Serving directory: {os.getcwd()}")
    print("Press Ctrl+C to stop the server")
    
    def start_server():
        httpd.serve_forever()
    
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    
    if open_browser:
        try:
            webbrowser.open(server_url)
        except Exception as e:
            print(f"Could not open browser: {e}")
            print(f"Please open {server_url} manually")
    
    try:
        while True:
            import time
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping server...")
        httpd.shutdown()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start a localhost HTTP server")
    parser.add_argument("-p", "--port", type=int, default=5173, help="Port number (default: 5173)")
    parser.add_argument("-d", "--directory", help="Directory to serve (default: current directory)")
    parser.add_argument("--no-browser", action="store_true", help="Don't open browser automatically")
    
    args = parser.parse_args()
    
    start_localhost_server(
        port=args.port,
        directory=args.directory,
        open_browser=not args.no_browser
    )

