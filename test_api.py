import requests
import json

# Test the Flask app endpoints
def test_endpoints():
    base_url = "http://localhost:5000"
    
    print("Testing Flask endpoints...")
    
    # Test 1: Check if server is running
    try:
        response = requests.get(f"{base_url}/")
        print(f"✅ Home page: Status {response.status_code}")
    except Exception as e:
        print(f"❌ Server not running: {e}")
        return
    
    # Test 2: Check roles endpoint
    try:
        response = requests.get(f"{base_url}/api/roles")
        print(f"✅ Roles API: Status {response.status_code}")
        print(f"   Roles: {response.json()}")
    except Exception as e:
        print(f"❌ Roles API error: {e}")
    
    # Test 3: Check roadmap endpoint
    try:
        data = {"role": "Python Developer", "level": "Beginner"}
        response = requests.post(
            f"{base_url}/api/roadmap",
            headers={"Content-Type": "application/json"},
            json=data
        )
        print(f"✅ Roadmap API: Status {response.status_code}")
        result = response.json()
        if result.get('success'):
            print(f"   Generated {len(result['roadmap'])} steps")
        else:
            print(f"   Error: {result.get('error')}")
    except Exception as e:
        print(f"❌ Roadmap API error: {e}")

if __name__ == "__main__":
    test_endpoints()