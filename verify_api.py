import urllib.request
import urllib.parse
import json

BASE_URL = "http://127.0.0.1:8000/api/dragons/"

def test_api():
    # 1. Create a dragon
    data = {
        "nom": "Smaug",
        "couleur": "Red",
        "categorie": "Fire",
        "taille": 150.5,
        "age": 500,
        "description": "Terrible and powerful"
    }
    # Encode data
    data_json = json.dumps(data).encode('utf-8')
    
    req = urllib.request.Request(BASE_URL, data=data_json, headers={'Content-Type': 'application/json'})
    
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 201:
                print("SUCCESS: Dragon created.")
                print(response.read().decode('utf-8'))
            else:
                print(f"FAILURE: Could not create dragon. Status: {response.status}")
                print(response.read().decode('utf-8'))
                return
    except urllib.error.URLError as e:
        print(f"FAILURE: Connection error: {e}")
        return

    # 2. List dragons
    try:
        with urllib.request.urlopen(BASE_URL) as response:
            if response.status == 200:
                print("SUCCESS: Listed dragons.")
                print(response.read().decode('utf-8'))
            else:
                print(f"FAILURE: Could not list dragons. Status: {response.status}")
    except urllib.error.URLError as e:
        print(f"FAILURE: Connection error: {e}")

if __name__ == "__main__":
    test_api()
