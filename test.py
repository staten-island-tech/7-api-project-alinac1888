import requests
headers = {
    "X-API-KEY": "9681c95b-6735-4bac-97fa-8d2f95d52242",
    "Accept-Version": "1.7.0"
}
import tkinter as tk
from tkinter import messagebox
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
        else:
            print("inavlid option")
            e.start()

    def choose_fish(e, fish, chances):
        return random.choices(fish, weights=chances, k=1)[0]
    
    def fishing(e):
        fish = ['tuna', 'salmon', 'sea bass', 'boot', 'squid', 'goldfish', 'red carp', 'fish poop', 'pike']
        chances = [1, 3, 3, 5, 2, 4, 4, 5, 1]
        bigchoice = input("Fish? y/n").lower()
        while bigchoice == "y":
            if e.fish_amoun > 0:
                catch = e.choose_fish(fish, chances)
                print(f"{e.vill} caught a {catch}!")
                e.inv.append(catch)
                e.fish_amoun -= 1
            elif e.fish_amoun == 0:
                print(f"{e.vill}'s line broke, here's all the fish you've caught: {e.inv}")
                break

            bigchoice = input("Fish? y/n").lower()
        if bigchoice == "n":
            print("say y when ur ready")
            e.fishing()
        else: 
            print("invalid choice try again")
            e.fishing()

# vill = villager([], 10)
# vill.start()

class FishingGame(tk.Tk):
    def __init__(self, villager):
        super().__init__()
        self.villager = villager
        self.title("Fishing Game")
        self.geometry("500x450")

        tk.Label(self, text="Choose your villager:", font=("Arial", 14)).pack(pady=10)

        self.villager_listbox = tk.Listbox(self)
        self.villager_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        self.start_button = tk.Button(self, text="Select Villager", command=self.choose_villager)
        self.start_button.pack(pady=5)

        self.fish_button = tk.Button(self, text="Fish!", command=self.fish, state=tk.DISABLED)
        self.fish_button.pack(pady=5)

        self.status_label = tk.Label(self, text="", font=("Arial", 12))
        self.status_label.pack(pady=10)

        self.reset_button = tk.Button(self, text="Reset Game", command=self.reset_game)
        self.reset_button.pack(pady=5)

        self.villager_data = []
        self.populate_villagers()

    def populate_villagers(self):
        url = "https://api.nookipedia.com/villagers"
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch villagers: {e}")
            self.destroy()
            return

        self.villager_data = data
        for v in data:
            self.villager_listbox.insert(tk.END, f"{v['name']} - {v['species']} - {v['personality']}")

    def choose_villager(self):
        selection = self.villager_listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a villager")
            return

        index = selection[0]
        chosen = self.villager_data[index]
        self.villager.vill = chosen["name"]
        self.villager.personality = chosen["personality"]
        self.status_label.config(text=f"Villager: {self.villager.vill} ({self.villager.personality})\nFish left: {self.villager.fish_amoun}")
        self.fish_button.config(state=tk.NORMAL)
        messagebox.showinfo("Villager Chosen", f"You chose {self.villager.vill}!")

    def fish(self):
        if self.villager.fish_amoun > 0:
            catch = self.villager.choose_fish()
            self.villager.inv.append(catch)
            self.villager.fish_amoun -= 1
            self.status_label.config(text=f"{self.villager.vill} caught a {catch}!\nFish left: {self.villager.fish_amoun}")
        else:
            messagebox.showinfo(
                "Line Broke",
                f"{self.villager.vill}'s line broke!\nYou caught: {', '.join(self.villager.inv)}"
            )
            self.fish_button.config(state=tk.DISABLED)

    def reset_game(self):
        self.villager.inv.clear()
        self.villager.fish_amoun = 10
        self.villager.vill = None
        self.villager.personality = None
        self.status_label.config(text="")
        self.fish_button.config(state=tk.DISABLED)
        self.villager_listbox.selection_clear(0, tk.END)
        messagebox.showinfo("Reset", "Game reset! Choose a new villager.")

vill = villager([], fishamoun=10)
app = FishingGame(vill)
app.mainloop()