#!/usr/bin/env python3
"""
Mock Backend Server for Quantum Banking App
Provides basic API endpoints for development without Docker
"""

import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import threading
import time

class MockBankingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = urlparse(self.path).path
        query_params = parse_qs(urlparse(self.path).query)
        
        # Handle CORS preflight
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()
        
        # Route handling
        if path == '/api/v1/health':
            response = {"status": "healthy", "service": "mock-backend", "timestamp": time.time()}
        elif path == '/api/v1/auth/me/' or path == '/api/v1/auth/me':
            response = {
                "id": "1",
                "email": "demo@quantumbank.com",
                "firstName": "Demo",
                "lastName": "User",
                "kycStatus": "verified",
                "isActive": True,
                "lastLogin": "2024-10-27T10:30:00Z"
            }
        elif path == '/api/v1/accounts/' or path == '/api/v1/accounts':
            response = [
                {
                    "id": 1,
                    "account_number": "QB-001-2024",
                    "balance": 15750.50,
                    "currency": "USD",
                    "account_type": "checking",
                    "status": "active"
                },
                {
                    "id": 2,
                    "account_number": "QB-002-2024", 
                    "balance": 5280.75,
                    "currency": "USD",
                    "account_type": "savings",
                    "status": "active"
                }
            ]
        elif path.startswith('/api/v1/accounts/transactions'):
            # Handle paginated transactions
            page = int(query_params.get('page', [1])[0])
            per_page = int(query_params.get('per_page', [10])[0])
            
            all_transactions = [
                {
                    "id": 1,
                    "amount": -45.99,
                    "description": "Coffee Shop Purchase",
                    "date": "2024-10-27T10:30:00Z",
                    "category": "food",
                    "status": "completed"
                },
                {
                    "id": 2,
                    "amount": 2500.00,
                    "description": "Salary Deposit",
                    "date": "2024-10-25T09:00:00Z",
                    "category": "income",
                    "status": "completed"
                },
                {
                    "id": 3,
                    "amount": -120.00,
                    "description": "Grocery Store",
                    "date": "2024-10-26T15:45:00Z",
                    "category": "shopping",
                    "status": "completed"
                },
                {
                    "id": 4,
                    "amount": -89.99,
                    "description": "Gas Station",
                    "date": "2024-10-24T08:20:00Z",
                    "category": "transport",
                    "status": "completed"
                }
            ]
            
            start_idx = (page - 1) * per_page
            end_idx = start_idx + per_page
            transactions = all_transactions[start_idx:end_idx]
            
            response = {
                "results": transactions,
                "count": len(all_transactions),
                "next": f"/api/v1/accounts/transactions/?page={page + 1}&per_page={per_page}" if end_idx < len(all_transactions) else None,
                "previous": f"/api/v1/accounts/transactions/?page={page - 1}&per_page={per_page}" if page > 1 else None
            }
        elif path.startswith('/api/v1/accounts/quick-actions'):
            response = [
                {"id": "transfer", "name": "Transfer Money", "icon": "arrow-right"},
                {"id": "pay", "name": "Pay Bills", "icon": "credit-card"},
                {"id": "deposit", "name": "Mobile Deposit", "icon": "camera"}
            ]
        elif path == '/api/v1/transactions':
            response = {
                "transactions": [
                    {
                        "id": 1,
                        "amount": -45.99,
                        "description": "Coffee Shop Purchase",
                        "date": "2024-10-27T10:30:00Z",
                        "category": "food",
                        "status": "completed"
                    },
                    {
                        "id": 2,
                        "amount": 2500.00,
                        "description": "Salary Deposit",
                        "date": "2024-10-25T09:00:00Z",
                        "category": "income",
                        "status": "completed"
                    }
                ]
            }
        elif path == '/api/v1/pqc/status':
            response = {
                "pqc_enabled": True,
                "algorithms": {
                    "key_encapsulation": "Kyber-768",
                    "digital_signature": "Dilithium-3"
                },
                "performance": {
                    "avg_encryption_time": "2.3ms",
                    "avg_decryption_time": "1.8ms"
                }
            }
        elif path.startswith('/api/v1/auth/webauthn/challenge'):
            # Handle WebAuthn challenge requests
            challenge_type = query_params.get('type', ['login'])[0]
            response = {
                "challenge": "mock_challenge_12345",
                "rpId": "localhost",
                "allowCredentials": [] if challenge_type == 'register' else [
                    {
                        "id": "mock_credential_id",
                        "type": "public-key"
                    }
                ]
            }
        # Handle service health checks
        elif path.endswith('/health/auth') or path.endswith('/health'):
            response = {"status": "healthy", "service": "mock-service"}
        # Handle missing endpoints that frontend expects
        elif path.startswith('/api/v1/pqc/') or path.startswith('/api/v1/kms/'):
            response = {
                "pqc_enabled": True,
                "algorithms": {"kyber": "768", "dilithium": "3"},
                "status": "operational"
            }
        elif path.startswith('/api/v1/fraud/'):
            response = {"risk_level": "low", "score": 0.1, "alerts": []}
        elif path.startswith('/api/v1/compliance/'):
            response = {"status": "compliant", "kyc_status": "verified"}
        elif path.startswith('/api/v1/notifications/'):
            response = {"notifications": [], "unread_count": 0}
        else:
            # Properly return 404 for unknown endpoints
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            response = {"error": "Endpoint not found", "path": path}
            self.wfile.write(json.dumps(response).encode())
            return
            
        self.wfile.write(json.dumps(response).encode())
    
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        try:
            request_body = json.loads(post_data.decode('utf-8')) if post_data else {}
        except:
            request_body = {}
        
        path = urlparse(self.path).path
        
        # Handle CORS
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()
        
        # Route handling
        if path == '/api/v1/auth/oauth2/token/' or path == '/api/v1/auth/login':
            response = {
                "user": {
                    "id": "1",
                    "email": request_body.get("email", "demo@quantumbank.com"),
                    "firstName": "Demo",
                    "lastName": "User",
                    "kycStatus": "verified",
                    "isActive": True,
                    "lastLogin": "2024-10-27T10:30:00Z"
                },
                "token": "mock_jwt_token_12345"
            }
        elif path == '/api/v1/auth/register/' or path == '/api/v1/auth/register':
            # Handle user registration
            print(f"📝 Registration request: {request_body}")
            
            # Validate required fields
            required_fields = ['email', 'password', 'firstName', 'lastName']
            missing_fields = [field for field in required_fields if not request_body.get(field)]
            
            if missing_fields:
                self.send_response(400)
                response = {
                    "error": f"Missing required fields: {', '.join(missing_fields)}",
                    "code": "VALIDATION_ERROR"
                }
            else:
                response = {
                    "user": {
                        "id": "2",
                        "email": request_body.get("email"),
                        "firstName": request_body.get("firstName"),
                        "lastName": request_body.get("lastName"),
                        "kycStatus": "pending",
                        "isActive": True,
                        "lastLogin": None
                    },
                    "token": "mock_jwt_token_67890"
                }
                print(f"✅ Registration successful for: {request_body.get('email')}")
        elif path == '/api/v1/auth/refresh/' or path == '/api/v1/auth/refresh':
            response = {
                "token": "mock_refreshed_jwt_token_12345"
            }
        elif path == '/api/v1/auth/logout/' or path == '/api/v1/auth/logout':
            response = {"message": "Successfully logged out"}
        elif path.startswith('/api/v1/auth/webauthn/verify'):
            # Handle WebAuthn verification
            response = {
                "user": {
                    "id": "1",
                    "email": "demo@quantumbank.com",
                    "firstName": "Demo",
                    "lastName": "User",
                    "kycStatus": "verified",
                    "isActive": True
                },
                "token": "mock_webauthn_token_12345"
            }
        elif path.startswith('/api/v1/auth/webauthn/enroll'):
            # Handle WebAuthn enrollment
            response = {"message": "Biometric enrollment successful"}
        elif path == '/api/v1/transactions':
            response = {
                "id": 5,
                "message": "Transaction created successfully",
                "status": "pending"
            }
        else:
            response = {"message": "Success", "path": path, "body": request_body}
            
        self.wfile.write(json.dumps(response).encode())
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()
    
    def log_message(self, format, *args):
        # Custom logging to show API calls
        print(f"🌐 API Call: {format % args}")

def run_server():
    server = HTTPServer(('localhost', 8080), MockBankingHandler)
    print("🚀 Mock Quantum Banking Backend Server")
    print("=" * 40)
    print("🌐 Server running on: http://localhost:8080")
    print("📋 Available endpoints:")
    print("   GET  /api/v1/health")
    print("   GET  /api/v1/auth/user") 
    print("   POST /api/v1/auth/login")
    print("   GET  /api/v1/accounts")
    print("   GET  /api/v1/transactions")
    print("   GET  /api/v1/pqc/status")
    print("=" * 40)
    print("✅ Ready to serve requests!")
    print("Press Ctrl+C to stop the server")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n⏹️  Server stopped")

if __name__ == "__main__":
    run_server()