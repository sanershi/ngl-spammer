import requests
import time
import threading
import colorama
from bs4 import BeautifulSoup
colorama.init()

print(colorama.Fore.LIGHTBLUE_EX)
colorama.init()
username = input("[*]" + colorama.Fore.LIGHTRED_EX+" Kullanıcı adı (Network'den bakın.): ")
colorama.init()
print(colorama.Fore.LIGHTBLUE_EX)
colorama.init()
msg = input("[*]" + colorama.Fore.LIGHTRED_EX+" Mesaj: ")
colorama.init()
print(colorama.Fore.LIGHTBLUE_EX)
colorama.init()

def send(username, msg):
    data = {
        "username": f"{username}",
        "question": f"{msg}",
        "deviceId": "550778a1-a038-43ff-b41a-3af4c248fa22",
        "gameSlug": "",
        "referrer": ""
    }

    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "tr-TR,tr;q=0.6",
        "content-length": "174",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://ngl.link",
        "referer": f"https://ngl.link/{username}",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sec-gpc": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }

    slm = requests.Session().post("https://ngl.link/api/submit", data=data, headers=headers)

    if slm.status_code == 200:
        print(colorama.Fore.LIGHTGREEN_EX+"Mesaj gönderildi")
        time.sleep(2)
    if slm.status_code != 200:
        print(colorama.Fore.LIGHTRED_EX+"Mesaj gönderilemedi timeout yedi!")

while True:
    try:
        send(username, msg)
    except:
        pass
