#===================[Coded By OnionTM]===================
from os import system
from requests import get
from colorama import Fore
from time import sleep
from sys import argv
#===================[BANNER]===================
def SlowPrint(txt):
    for x in txt:
        print(x, end="", flush=True)
        sleep(0.001)
    print()
admin = get("https://raw.githubusercontent.com/the-c0d3r/admin-finder/master/wordlists/wordlist.txt").text.splitlines()
if len(argv) < 2:
    print("""

  /$$$$$$            /$$                  /$$$$$$$$ /$$      /$$
 /$$__  $$          |__/                 |__  $$__/| $$$    /$$$
| $$  \ $$ /$$$$$$$  /$$  /$$$$$$  /$$$$$$$ | $$   | $$$$  /$$$$
| $$  | $$| $$__  $$| $$ /$$__  $$| $$__  $$| $$   | $$ $$/$$ $$
| $$  | $$| $$  \ $$| $$| $$  \ $$| $$  \ $$| $$   | $$  $$$| $$
| $$  | $$| $$  | $$| $$| $$  | $$| $$  | $$| $$   | $$\  $ | $$
|  $$$$$$/| $$  | $$| $$|  $$$$$$/| $$  | $$| $$   | $$ \/  | $$
 \______/ |__/  |__/|__/ \______/ |__/  |__/|__/   |__/     |__/

[!] Onion AdminPanel Scanner
[!] Usage : python OnionAdmin.py <link>

""")
elif len(argv) == 2:
    print("""

  /$$$$$$            /$$                  /$$$$$$$$ /$$      /$$
 /$$__  $$          |__/                 |__  $$__/| $$$    /$$$
| $$  \ $$ /$$$$$$$  /$$  /$$$$$$  /$$$$$$$ | $$   | $$$$  /$$$$
| $$  | $$| $$__  $$| $$ /$$__  $$| $$__  $$| $$   | $$ $$/$$ $$
| $$  | $$| $$  \ $$| $$| $$  \ $$| $$  \ $$| $$   | $$  $$$| $$
| $$  | $$| $$  | $$| $$| $$  | $$| $$  | $$| $$   | $$\  $ | $$
|  $$$$$$/| $$  | $$| $$|  $$$$$$/| $$  | $$| $$   | $$ \/  | $$
 \______/ |__/  |__/|__/ \______/ |__/  |__/|__/   |__/     |__/

[!] Onion AdminPanel Scanner
[!] Coded By OnionTM

""")
#===================[CHECK]===================
    for a in admin:
        try:
            url = str(argv[1])+str(a)
            r = get(url)
            if r.status_code == 200:
                print(F"""
[+] FOUND

-------------------------------------------
URL : {str(argv[1])}

Admin Page : {url}
-------------------------------------------
""")
                break
            else:
                print("[-] NOT FOUND : "+url)
        except KeyboardInterrupt:
            exit()
#==================[########]===================
#           https://Github.com/OnionTM
#==================[########]===================
