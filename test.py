import requests
headers = {
    "X-API-KEY": "9681c95b-6735-4bac-97fa-8d2f95d52242",
    "Accept-Version": "1.7.0"
}
import tkinter as tk
import random

class villager:
    def __init__(e, inv):
        e.vill = None
        e.inv = inv
        inv = []
        e.personality = None

    def start(e):
        star = input("wanna start? y/n")
        if star == "y":
            url = "https://api.nookipedia.com/villagers"
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                print("Error fetching data!")

            data = response.json()
            for villager in data:
                print(f"name: {villager['name']} - personality: {villager['personality']}")
            while True:
                choice = input("what villager")
                if choice == villager:
                    print(f"{choice} yay")
                    e.vill = choice
                    break
                else:
                    print("sorry its not a villager")
                        
        elif star == "n":
            print("say y when ur ready")
            e.start()

    def fishing(e):
        import random
        if e.fishamoun > 0:
            random.choice(e.loot)
            print(f"you caught a {e.loot}")
        if e.fishamoun <= 0:
            print("sorry your line broke")

vill = villager([])
vill.start()
