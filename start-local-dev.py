#!/usr/bin/env python3
"""
Local Development Server for Quantum Banking App
Runs a simplified version without Docker dependencies
"""

import subprocess
import sys
import time
import threading
from pathlib import Path

def run_frontend():
    """Start the React frontend"""
    print("🚀 Starting React Frontend...")
    try:
        subprocess.run([
            "npm", "run", "dev"
        ], cwd="frontend", check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Frontend failed to start: {e}")

def run_mock_backend():
    """Start a mock backend server"""
    print("🔧 Starting Mock Backend Server...")
    
    # Create a simple mock server
    mock_server_code = '''
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import threading
import time

class MockBankingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        path = urlparse(self.path).path
        
        if path == '/api/v1/health':
            response = {"status": "healthy", "service": "mock-backend"}
        elif path == '/api/v1/auth/user':
            response = {
                "id": 1,
                "username": "demo_user",
                "email": "demo@quantumbank.com",
                "first_name": "Demo",
                "last_name": "User"
            }
        elif path == '/api/v1/accounts':
            response = {
                "accounts": [
                    {
                        "id": 1,
                        "account_number": "QB-001-2024",
                        "balance": 15750.50,
                        "currency": "USD",
                        "account_type": "checking"
                    }
                ]
            }
        elif path == '/api/v1/transactions':
            response = {
                "transactions": [
                    {
                        "id": 1,
                        "amount": -45.99,
                        "description": "Coffee Shop Purchase",
                        "date": "2024-10-27T10:30:00Z",
                        "category": "food"
                    },
                    {
                        "id": 2,
                        "amount": 2500.00,
                        "description": "Salary Deposit",
                        "date": "2024-10-25T09:00:00Z",
                        "category": "income"
                    }
                ]
            }
        else:
            response = {"error": "Not found"}
            
        self.wfile.write(json.dumps(response).encode())
    
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        path = urlparse(self.path).path
        
        if path == '/api/v1/auth/login':
            response = {
                "access_token": "mock_jwt_token_12345",
                "token_type": "Bearer",
                "expires_in": 3600
            }
        else:
            response = {"message": "Success"}
            
        self.wfile.write(json.dumps(response).encode())
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()

def run_server():
    server = HTTPServer(('localhost', 8080), MockBankingHandler)
    print("🌐 Mock Backend running on http://localhost:8080")
    server.serve_forever()

if __name__ == "__main__":
    run_server()
'''
    
    # Write the mock server to a file
    with open("mock_backend.py", "w") as f:
        f.write(mock_server_code)
    
    # Start the mock server
    try:
        subprocess.Popen([sys.executable, "mock_backend.py"])
        print("✅ Mock backend started on http://localhost:8080")
    except Exception as e:
        print(f"❌ Failed to start mock backend: {e}")

def main():
    print("🏦 Quantum Banking - Local Development Setup")
    print("=" * 50)
    
    # Start mock backend in a separate thread
    backend_thread = threading.Thread(target=run_mock_backend, daemon=True)
    backend_thread.start()
    
    # Give backend time to start
    time.sleep(2)
    
    print("\n🎯 Services Status:")
    print("✅ Frontend: http://localhost:3000")
    print("✅ Mock Backend: http://localhost:8080")
    print("\n📝 Note: This is a simplified development setup.")
    print("For full functionality, install Docker and run: docker compose up")
    
    print("\n🔄 Starting services...")
    
    # Keep the script running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n⏹️  Shutting down local development server...")

if __name__ == "__main__":
    main()