import requests

def get(villager):
    url = "https://api.animalcrossing.com/data"
    key = "9681c95b-6735-4bac-97fa-8d2f95d52242"
    headers = {
    "Authorization": f"Bearer {key}"
    }
    response = requests.get(f"api.nookipedia.com"(villager.lower()))
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "villager": data["villager"]
    }

villager = get("Daisy")
print(villager)