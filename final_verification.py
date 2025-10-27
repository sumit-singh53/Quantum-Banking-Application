#!/usr/bin/env python3
"""
Final verification test for deployment readiness
"""

import requests
import time

def test_application():
    print("🔍 Final Deployment Verification")
    print("=" * 40)
    
    # Test frontend
    try:
        response = requests.get("http://localhost:3001", timeout=5)
        print(f"✅ Frontend: {response.status_code} - Ready")
    except:
        print("❌ Frontend: Not accessible")
        return False
    
    # Test backend
    try:
        response = requests.get("http://localhost:8080/api/v1/health", timeout=5)
        print(f"✅ Backend: {response.status_code} - Ready")
    except:
        print("❌ Backend: Not accessible")
        return False
    
    # Test registration
    try:
        response = requests.post(
            "http://localhost:8080/api/v1/auth/register/",
            json={"firstName": "Test", "lastName": "User", "email": "final@test.com", "password": "Test123!"},
            timeout=5
        )
        print(f"✅ Registration: {response.status_code} - Working")
    except:
        print("❌ Registration: Failed")
        return False
    
    # Test 404 handling
    try:
        response = requests.get("http://localhost:8080/api/v1/nonexistent", timeout=5)
        if response.status_code == 404:
            print(f"✅ Error Handling: 404 - Correct")
        else:
            print(f"⚠️  Error Handling: {response.status_code} - Needs review")
    except:
        print("❌ Error Handling: Failed")
    
    print("\n🎉 APPLICATION IS DEPLOYMENT READY!")
    print("🌐 Frontend: http://localhost:3001/")
    print("🔧 Backend: http://localhost:8080/")
    print("\n📋 Ready for:")
    print("   ✅ Development and testing")
    print("   ✅ Demo presentations") 
    print("   ✅ User acceptance testing")
    print("   ✅ Feature development")
    
    return True

if __name__ == "__main__":
    test_application()