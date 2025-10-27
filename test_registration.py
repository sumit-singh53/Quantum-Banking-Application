#!/usr/bin/env python3
"""
Test registration endpoint
"""

import requests
import json

def test_registration():
    base_url = "http://localhost:8080"
    
    print("🧪 Testing Registration Endpoint")
    print("=" * 35)
    
    # Test registration
    registration_data = {
        "firstName": "John",
        "lastName": "Doe", 
        "email": "john.doe@example.com",
        "password": "SecurePassword123!"
    }
    
    try:
        response = requests.post(
            f"{base_url}/api/v1/auth/register/",
            json=registration_data,
            headers={"Content-Type": "application/json"}
        )
        print(f"✅ Registration: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   User ID: {data['user']['id']}")
            print(f"   Email: {data['user']['email']}")
            print(f"   Name: {data['user']['firstName']} {data['user']['lastName']}")
            print(f"   Token: {data['token'][:20]}...")
        else:
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"❌ Registration failed: {e}")
    
    # Test login
    login_data = {
        "email": "john.doe@example.com",
        "password": "SecurePassword123!"
    }
    
    try:
        response = requests.post(
            f"{base_url}/api/v1/auth/oauth2/token/",
            json=login_data,
            headers={"Content-Type": "application/json"}
        )
        print(f"✅ Login: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   Token: {data['token'][:20]}...")
        else:
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"❌ Login failed: {e}")

if __name__ == "__main__":
    test_registration()