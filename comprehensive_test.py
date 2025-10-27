#!/usr/bin/env python3
"""
Comprehensive test suite for the Quantum Banking Application
Tests all critical components and endpoints for deployment readiness
"""

import requests
import json
import time
from urllib.parse import urljoin

class QuantumBankingTester:
    def __init__(self):
        self.frontend_url = "http://localhost:3001"
        self.backend_url = "http://localhost:8080"
        self.test_results = []
        
    def log_test(self, test_name, success, message="", details=None):
        """Log test results"""
        status = "✅ PASS" if success else "❌ FAIL"
        self.test_results.append({
            "test": test_name,
            "success": success,
            "message": message,
            "details": details
        })
        print(f"{status} {test_name}: {message}")
        
    def test_frontend_availability(self):
        """Test if frontend is accessible"""
        try:
            response = requests.get(self.frontend_url, timeout=10)
            success = response.status_code == 200
            self.log_test(
                "Frontend Availability", 
                success,
                f"Status: {response.status_code}" if success else "Frontend not accessible"
            )
            return success
        except Exception as e:
            self.log_test("Frontend Availability", False, f"Error: {str(e)}")
            return False
    
    def test_backend_health(self):
        """Test backend health endpoint"""
        try:
            response = requests.get(f"{self.backend_url}/api/v1/health", timeout=5)
            success = response.status_code == 200
            data = response.json() if success else None
            self.log_test(
                "Backend Health", 
                success,
                f"Service: {data.get('service', 'unknown')}" if data else "Health check failed"
            )
            return success
        except Exception as e:
            self.log_test("Backend Health", False, f"Error: {str(e)}")
            return False
    
    def test_auth_endpoints(self):
        """Test authentication endpoints"""
        endpoints = [
            ("/api/v1/auth/register/", "POST", {"firstName": "Test", "lastName": "User", "email": "test@example.com", "password": "Test123!"}),
            ("/api/v1/auth/oauth2/token/", "POST", {"email": "test@example.com", "password": "Test123!"}),
            ("/api/v1/auth/me/", "GET", None),
            ("/api/v1/auth/refresh/", "POST", {}),
        ]
        
        all_passed = True
        for endpoint, method, data in endpoints:
            try:
                url = f"{self.backend_url}{endpoint}"
                if method == "GET":
                    response = requests.get(url, timeout=5)
                else:
                    response = requests.post(url, json=data, timeout=5)
                
                success = response.status_code in [200, 201]
                self.log_test(
                    f"Auth Endpoint {method} {endpoint}",
                    success,
                    f"Status: {response.status_code}"
                )
                if not success:
                    all_passed = False
            except Exception as e:
                self.log_test(f"Auth Endpoint {method} {endpoint}", False, f"Error: {str(e)}")
                all_passed = False
        
        return all_passed
    
    def test_api_endpoints(self):
        """Test main API endpoints"""
        endpoints = [
            "/api/v1/accounts/",
            "/api/v1/accounts/transactions/?page=1&per_page=10",
            "/api/v1/accounts/quick-actions/",
            "/api/v1/pqc/status",
            "/api/v1/transactions",
        ]
        
        all_passed = True
        for endpoint in endpoints:
            try:
                response = requests.get(f"{self.backend_url}{endpoint}", timeout=5)
                success = response.status_code == 200
                self.log_test(
                    f"API Endpoint {endpoint}",
                    success,
                    f"Status: {response.status_code}"
                )
                if not success:
                    all_passed = False
            except Exception as e:
                self.log_test(f"API Endpoint {endpoint}", False, f"Error: {str(e)}")
                all_passed = False
        
        return all_passed
    
    def test_cors_headers(self):
        """Test CORS configuration"""
        try:
            response = requests.options(f"{self.backend_url}/api/v1/health")
            cors_headers = {
                'Access-Control-Allow-Origin': response.headers.get('Access-Control-Allow-Origin'),
                'Access-Control-Allow-Methods': response.headers.get('Access-Control-Allow-Methods'),
                'Access-Control-Allow-Headers': response.headers.get('Access-Control-Allow-Headers'),
            }
            
            success = all(header for header in cors_headers.values())
            self.log_test(
                "CORS Configuration",
                success,
                "All CORS headers present" if success else "Missing CORS headers",
                cors_headers
            )
            return success
        except Exception as e:
            self.log_test("CORS Configuration", False, f"Error: {str(e)}")
            return False
    
    def test_error_handling(self):
        """Test error handling for non-existent endpoints"""
        try:
            response = requests.get(f"{self.backend_url}/api/v1/nonexistent", timeout=5)
            success = response.status_code == 404
            self.log_test(
                "Error Handling",
                success,
                f"404 returned for non-existent endpoint" if success else f"Unexpected status: {response.status_code}"
            )
            return success
        except Exception as e:
            self.log_test("Error Handling", False, f"Error: {str(e)}")
            return False
    
    def test_data_consistency(self):
        """Test data consistency across endpoints"""
        try:
            # Test accounts endpoint
            accounts_response = requests.get(f"{self.backend_url}/api/v1/accounts/", timeout=5)
            if accounts_response.status_code != 200:
                self.log_test("Data Consistency", False, "Accounts endpoint failed")
                return False
            
            accounts_data = accounts_response.json()
            has_accounts = len(accounts_data) > 0
            
            # Test transactions endpoint
            transactions_response = requests.get(f"{self.backend_url}/api/v1/accounts/transactions/?page=1&per_page=10", timeout=5)
            if transactions_response.status_code != 200:
                self.log_test("Data Consistency", False, "Transactions endpoint failed")
                return False
            
            transactions_data = transactions_response.json()
            has_transactions = 'results' in transactions_data and len(transactions_data['results']) > 0
            
            success = has_accounts and has_transactions
            self.log_test(
                "Data Consistency",
                success,
                f"Accounts: {len(accounts_data)}, Transactions: {len(transactions_data.get('results', []))}"
            )
            return success
        except Exception as e:
            self.log_test("Data Consistency", False, f"Error: {str(e)}")
            return False
    
    def test_performance(self):
        """Test basic performance metrics"""
        try:
            start_time = time.time()
            response = requests.get(f"{self.backend_url}/api/v1/health", timeout=5)
            response_time = (time.time() - start_time) * 1000  # Convert to milliseconds
            
            success = response.status_code == 200 and response_time < 1000  # Less than 1 second
            self.log_test(
                "Performance",
                success,
                f"Response time: {response_time:.2f}ms" if success else f"Slow response: {response_time:.2f}ms"
            )
            return success
        except Exception as e:
            self.log_test("Performance", False, f"Error: {str(e)}")
            return False
    
    def run_all_tests(self):
        """Run all tests and generate report"""
        print("🔍 Starting Comprehensive Quantum Banking Application Test")
        print("=" * 60)
        
        tests = [
            self.test_frontend_availability,
            self.test_backend_health,
            self.test_auth_endpoints,
            self.test_api_endpoints,
            self.test_cors_headers,
            self.test_error_handling,
            self.test_data_consistency,
            self.test_performance,
        ]
        
        for test in tests:
            test()
            time.sleep(0.5)  # Brief pause between tests
        
        # Generate summary
        total_tests = len(self.test_results)
        passed_tests = sum(1 for result in self.test_results if result['success'])
        failed_tests = total_tests - passed_tests
        
        print("\n" + "=" * 60)
        print("📊 TEST SUMMARY")
        print("=" * 60)
        print(f"Total Tests: {total_tests}")
        print(f"✅ Passed: {passed_tests}")
        print(f"❌ Failed: {failed_tests}")
        print(f"Success Rate: {(passed_tests/total_tests)*100:.1f}%")
        
        if failed_tests == 0:
            print("\n🎉 ALL TESTS PASSED - APPLICATION IS DEPLOYMENT READY!")
            print("🌐 Frontend: http://localhost:3001/")
            print("🔧 Backend: http://localhost:8080/")
        else:
            print(f"\n⚠️  {failed_tests} TESTS FAILED - REVIEW REQUIRED")
            print("\nFailed Tests:")
            for result in self.test_results:
                if not result['success']:
                    print(f"   ❌ {result['test']}: {result['message']}")
        
        return failed_tests == 0

if __name__ == "__main__":
    tester = QuantumBankingTester()
    success = tester.run_all_tests()
    exit(0 if success else 1)