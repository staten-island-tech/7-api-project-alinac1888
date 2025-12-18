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
    
    # data = response.json()
    # print(data)

    # return {
    #     "name": data["name"],
    #     "species": data["species"],
    #     "personality": data["personality"],
    #     "phrase": data["phrase"]
    #         }
    
get()

import tkinter
tk = tkinter

window = tk.Tk()
window.title("YAY")
window.geometry("400x250")
window.resizable(False, False)
prompt = tk.Label(window, text="nahahahahahahhaah",
font=("Times New Roman", 14))
prompt.pack(pady=10)