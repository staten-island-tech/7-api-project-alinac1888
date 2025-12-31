import requests
headers = {
    "X-API-KEY": "9681c95b-6735-4bac-97fa-8d2f95d52242",
    "Accept-Version": "1.7.0"
}

class villager:
    def __init__(e, vill, inv, fishamoun, sea):
        e.vill = vill
        e.inv = inv
        e.fishamoun = fishamoun
        e.sea = sea
        sea = 10
        inv = []

    def get():
        url = "https://api.nookipedia.com/villagers"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print("Error fetching data!")
            return None
    
        data = response.json()
        return {
        "name": data["name"],
        "species": data["species"],
        "personality": data["personality"],
        "phrase": data["phrase"]
            }

    def start(e, data):
        print(data["name"])
        choice = input("what villager")
        if choice == data["name"]:
            print(f"{choice} yay")
        else:
            print("sorry its not a villager")
            e.start(choice = input("what villager"))