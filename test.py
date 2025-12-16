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
    
    data = response.json()
    print(data)

get()