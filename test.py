import requests
headers = {
    "X-API-KEY": "9681c95b-6735-4bac-97fa-8d2f95d52242",
    "Accept-Version": "1.7.0"
}
import tkinter as tk
import random

class villager:
    def __init__(e, inv, fishamoun):
        e.vill = None
        e.inv = inv
        inv = []
        e.personality = None
        e.fish_amoun = fishamoun

    def start(e):
        star = input("wanna start? y/n").lower()
        if star == "y":
            url = "https://api.nookipedia.com/villagers"
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                print("Error fetching data!")

            data = response.json()

            villager_n = []

            for villager in data:
                name = villager["name"]
                villager_n.append(name)
                print(f"name: {name} - species: {villager['species']} - personality: {villager['personality']}")
            while True:
                choice = input("what villager")
                if choice in villager_n:
                    print(f"{choice} yay")
                    e.vill = choice
                    e.personality = {villager['personality']}
                    e.fishing()
                    break
                else:
                    print("sorry its not a villager")
                        
        elif star == "n":
            print("say y when ur ready")
            e.start()

    def fishing(e):
        fish = ['tuna', 'salmon', 'sea bass', 'boot', 'squid', 'goldfish', 'red carp', 'fish poop', 'pike']
        chances = [2, 1, 1, 0, 2, 1, 1, 0, 2000]
        bigchoice = input("Fish? y/n").lower()
        while bigchoice == "y":
            if e.fish_amoun > 0:
                catch = random.choice(fish)
                print(f"You caught a {catch}!")
                catch += e.fish_amoun
                break
            else:
                print("your line broke")
        if bigchoice == "n":
            print("say y when ur ready")
            e.fishing()

vill = villager([], 10)
vill.start()
