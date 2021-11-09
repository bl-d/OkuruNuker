import os, ctypes, sys, requests
from colorama import Fore, init

init()

class util:
    def setTitle(title: str) -> str:
        if os.name == 'nt':
            ctypes.windll.kernel32.SetConsoleTitleW(title)
            return(True)
        else:
            #print("\33]0;" + title)
            return(False)

    def getList(fileName: str) -> list:
        try:
            with open(fileName, 'r') as f:
                content = f.read().splitlines()
                f.close()
            return(content)
        except FileNotFoundError:
            return([])

    def checkToken(token: str) -> str:
        request = requests.get(
            'https://discord.com/api/v9/users/@me', 
            headers={'Authorization': token}
        )
        if request.status_code == 200:
            return('user')
        else:
            return('bot')

    def cls():
        # could do os.system('cls' if os.name == 'nt' else 'clear')
        # but this looks "cleaner"
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        return(True)

    def log(prefix: str, message: str, end: str = '\n'):
        return(sys.stdout.write(f'{Fore.LIGHTBLUE_EX}{prefix} {Fore.RESET}{message}{end}'))
