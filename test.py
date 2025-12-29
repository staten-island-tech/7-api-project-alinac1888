import requests
headers = {
    "X-API-KEY": "9681c95b-6735-4bac-97fa-8d2f95d52242",
    "Accept-Version": "1.7.0"
}
def get():

    url = "https://api.nookipedia.com/villagers"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    url = "https://api.nookipedia.com/nh/fish"
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

get()
# import tkinter as tk
# window = tk.Tk()
# window.title("fishing")
# window.geometry("400x250")
# window.resizable(False, False)
# prompt = tk.Label(window, text="nanana", font= ("Arial", 14))
# prompt.pack(pady=10)
# entry = tk.Entry(window, font=("Arial", 14), width=30)
# entry.pack(pady=5)
# result_label = tk.Label(window, text="", font=("Arial", 14, "bold"), fg="blue")
# result_label.pack(pady=15)
# def reverse_message():
#     text = entry.get()
#     reversed_text = text[::-1]
#     result_label.config(text=f"Backwards: {reversed_text}")
# reverse_button = tk.Button(window, text="Reverse Message!", font=("Arial", 14), command=reverse_message)
# reverse_button.pack(pady=10)
# window.mainloop()

class villager:
    def _init_(e, vill, inv, fishamoun, sea):
        e.vill = vill
        e.inv = inv
        e.fishamoun = fishamoun
        e.sea = sea
        sea = 10

    def start(e, data):
        print(data["name"])
        choice = input("what villager")
        if choice == data["name"]:
            print(f"{choice} yay")
        else:
            print("sorry its not a villager")
            e.start(choice = input("what villager"))
        