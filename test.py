import requests
headers = {
    "X-API-KEY": "9681c95b-6735-4bac-97fa-8d2f95d52242",
    "Accept-Version": "1.7.0"
}

class villager:
    def __init__(e, vill, fishamoun, loot):
        e.vill = vill
        e.inv = []
        e.fishamoun = fishamoun
        fishamoun = 10
        e.loot = fish
        fish = ["tuna", "salmon", "sea bass", "boot"]

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

    def fishing(e):
        import random
        if e.fishamoun > 0:
            random.choice(e.loot)
            print(f"you caught a {e.loot}")
        if e.fishamoun <= 0:
            print("sorry your line broke")

    import tkinter as tk
    import random

    def __init__(self, root):
            self.root = root
            self.root.title("Fishing Game")

            self.title_label = tk.Label(root, text="Choose Your Character", font=("Arial", 14))
            self.title_label.pack(pady=10)

            self.character_var = tk.StringVar()
            self.character_var.set(self.characters[0])

            self.dropdown = tk.OptionMenu(root, self.character_var, *self.characters)
            self.dropdown.pack()

            self.select_button = tk.Button(
            root, text="Select Character", command=self.select_character
            )
            self.select_button.pack(pady=10)

            self.info_label = tk.Label(root, text="", font=("Times New Roman", 11))
            self.info_label.pack(pady=10)

            self.fish_button = tk.Button(
            root, text="Go Fishing", command=self.fish, state="disabled"
            )
            self.fish_button.pack(pady=5)

        def select_character(self):
            self.selected_character = self.character_var.get()
            self.info_label.config(
                text=f"You are now playing as {self.selected_character}!\nFish left: {self.fish_left}"
            )
            self.fish_button.config(state="normal")

        def fish(self):
            if self.fish_left > 0:
                caught = random.choice(self.loot)
                self.fish_left -= 1
                self.info_label.config(
                    text=f"{self.selected_character} caught a {caught}!\n"
                        f"Fish left: {self.fish_left}"
                        )
            else:
                self.info_label.config(
                    text=f"{self.selected_character}'s fishing rod broke!"
                )
                self.fish_button.config(state="disabled")


    root = tk.Tk()
    app = FishingApp(root)
    root.mainloop()
