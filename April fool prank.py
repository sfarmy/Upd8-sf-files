import random
from threading import Lock
from cfonts import render



color_combinations = [
    ['red', 'yellow'],
    ['blue', 'cyan'],
    ['green', 'white'],
    ['magenta', 'cyan'],
    ['yellow', 'red'],
    ['cyan', 'blue'],
    ['white', 'green'],
    ['red', 'white'],
    ['blue', 'magenta'],
    ['green', 'yellow']
]

red = "\033[1m\033[31m"
green = "\033[1m\033[32m"
yellow = "\033[1m\033[33m"
blue = "\033[1m\033[34m"
cyan = "\033[1m\033[36m"
magenta = "\033[1m\033[35m"
white = "\033[1m\033[37m"
orange = "\033[1m\033[38;5;208m"
reset = "\033[0m"
GOLD   = '\033[38;5;220m'
SILVER = '\033[38;5;250m'
PURPLE = '\033[38;5;129m'

random_colors = random.choice(color_combinations)
MAIN_TITLE = render('     SF     SPECIAL FILE ', colors=random_colors, align='center')
LOCKER=Lock()
USED=set()
print(MAIN_TITLE)

print(f"{' ' * 31}{cyan}TELEGRAM ➤  {white}@SHADOWFIGHTER05")
print(f"{' ' * 31}{cyan}    JOIN ➤  {white}@SF_ARMY\n")


import time
import os
import random

RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
WHITE = "\033[97m"
RESET = "\033[0m"


bot_token = input(f" {RED} 🤖 𝐁𝐨𝐭 𝐭𝐨𝐤𝐞𝐧 : ")
chat_id = input(f"  🆔 𝐂𝐡𝐚𝐭 𝐈𝐃 : {RESET}")

print(GREEN + "\n⚡ Initializing System...\n" + RESET)
time.sleep(2)

hit = 0
gen = 0
good = 0

for i in range(10):
    gen += random.randint(2, 5)
    good += random.randint(1, 3)
    print(CYAN + f"💻 Hit: {hit} | Gen: {gen} | Good: {good}" + RESET, end="\r")
    time.sleep(1)

hit += 100
print(YELLOW + "\n\n⚡ BOOST MODE ENABLED ⚡\n" + RESET)
time.sleep(2)
print(GREEN + f"💻 Hit: {hit} | Gen: {gen} | Good: {good}" + RESET)

time.sleep(2)
print(RED + "\n❌ Please fix your internet...\n" + RESET)
time.sleep(3)

for i in range(6):
    hit += random.randint(10, 25)
    gen += random.randint(5, 10)
    good += random.randint(2, 6)
    print(YELLOW + f"💻 Hit: {hit} | Gen: {gen} | Good: {good}" + RESET, end="\r")
    time.sleep(1)

print("\n")

# LOADING #
def loading(text):
    print(YELLOW + text + RESET)
    for i in range(0, 101, 5):
        bar = "█" * (i//5) + "-" * (20 - i//5)
        print(f"\r[{bar}] {i}%", end="")
        time.sleep(0.08)
    print("\n")

loading("🔄 Connecting to server...")
loading("📡 Syncing data...")


print(GREEN + "\n💻 Activating Matrix Interface...\n" + RESET)
time.sleep(1)

start = time.time()

while time.time() - start < 5:   
    line = ''.join(random.choices("01", k=60))
    print(GREEN + line + RESET)
    time.sleep(0.04)
    
#hacking
print(RED + "\n💀 INITIATING HACK...\n" + RESET)

commands = [
    "nmap scanning...",
    "injecting payload...",
    "bypassing firewall...",
    "decrypting database...",
    "access granted...",
    "root access achieved...",
    "stealing data...",
    "creating backdoor..."
]

start = time.time()
while time.time() - start < 10:
    print(GREEN + "> " + random.choice(commands) + RESET)
    time.sleep(0.1)

#VIRUS 
print(RED + "\n☣️ TROJAN VIRUS DETECTED ☣️\n" + RESET)
time.sleep(1)

for i in range(0, 101, 10):
    print(RED + f"💣 Infection Progress: {i}%" + RESET)
    time.sleep(0.4)

# countdown 
print(RED + "\n⏳ SYSTEM WILL CRASH IN...\n" + RESET)
for i in range(5, 0, -1):
    print(RED + f"💥 {i}..." + RESET)
    time.sleep(1)

print(RED + "\n🛑 DEVICE SUSPENDED 🛑\n" + RESET)
time.sleep(2)

os.system("cls" if os.name == "nt" else "clear")

def center_text(text):
    width = 60
    return text.center(width)

def slow_line(text, color):
    for char in text:
        print(color + char + RESET, end='', flush=True)
        time.sleep(0.01)
    print()

for _ in range(2):
    print(RED + "\n⚠️ SYSTEM FAILURE ⚠️\n" + RESET)
    time.sleep(0.4)
    os.system("cls" if os.name == "nt" else "clear")

print("\n")

slow_line(center_text("😂 IT'S A PRANK 😂"), GREEN)
time.sleep(0.5)
slow_line(center_text("🎉 HAPPY APRIL FOOL DAY 🎉"), YELLOW)
time.sleep(0.5)
slow_line(center_text("😎 JUST MASTI BRO!"), CYAN)

print("\n")

print(WHITE + center_text("😂 THIS IS ONLY A PRANK TOOL NOTHING ELSE") + RESET)
print(WHITE + center_text("AGAR KISKO HURT HUA HO TO MAAF KARAN 😁") + RESET)