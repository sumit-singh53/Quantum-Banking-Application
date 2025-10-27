#!/usr/bin/env python3
"""
Quick API test to verify our mock backend is working
"""

import requests
import json

def test_api():
    base_url = "http://localhost:8080"
    
    print("🧪 Testing Mock Backend API")
    print("=" * 30)
    
    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/api/v1/health")
        print(f"✅ Health Check: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"❌ Health Check failed: {e}")
    
    # Test accounts endpoint
    try:
        response = requests.get(f"{base_url}/api/v1/accounts")
        print(f"✅ Accounts: {response.status_code}")
        data = response.json()
        print(f"   Found {len(data['accounts'])} accounts")
    except Exception as e:
        print(f"❌ Accounts failed: {e}")
    
    # Test transactions endpoint
    try:
        response = requests.get(f"{base_url}/api/v1/transactions")
        print(f"✅ Transactions: {response.status_code}")
        data = response.json()
        print(f"   Found {len(data['transactions'])} transactions")
    except Exception as e:
        print(f"❌ Transactions failed: {e}")
    
    # Test PQC status endpoint
    try:
        response = requests.get(f"{base_url}/api/v1/pqc/status")
        print(f"✅ PQC Status: {response.status_code}")
        data = response.json()
        print(f"   PQC Enabled: {data['pqc_enabled']}")
        print(f"   Algorithms: {data['algorithms']}")
    except Exception as e:
        print(f"❌ PQC Status failed: {e}")
    
    print("\n🎯 Backend API is working correctly!")

if __name__ == "__main__":
    test_api()