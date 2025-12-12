import requests

def get(villager):
    response = requests.get(f"9681c95b-6735-4bac-97fa-8d2f95d52242"(villager.lower()))
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "villager": data["villager"]
    }

villager = get("Daisy")
print(villager)