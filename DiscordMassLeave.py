import requests

TOKEN = "Token here"
HEADERS = {"Authorization": TOKEN, "User-Agent": "Mozilla/5.0"}

try:
    guilds = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=HEADERS).json()
except:
    print("Error fetching servers")
    exit()

for g in guilds:
    r = input(f"Leave server '{g['name']}'? (y/n) ").lower()
    if r == "y":
        resp = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{g['id']}", headers=HEADERS)
        if resp.status_code == 204:
            print(f"Left server: {g['name']}")
        else:
            print(f"Failed to leave server: {g['name']} (status {resp.status_code})")
    else:
        print(f"Kept server: {g['name']}")
