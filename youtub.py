from os import system as c
import time
import random

# Colors
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
B = '\x1b[38;5;51m'
P = '\x1b[38;5;201m'

# Logo
def logo():
    c('clear')
    print(f"""{R}
██╗   ██╗██╗   ██╗████████╗ ██████╗ 
██║   ██║██║   ██║╚══██╔══╝██╔═══██╗
██║   ██║██║   ██║   ██║   ██║   ██║
╚██╗ ██╔╝██║   ██║   ██║   ██║   ██║
 ╚████╔╝ ╚██████╔╝   ██║   ╚██████╔╝
  ╚═══╝   ╚═════╝    ╚═╝    ╚═════╝ 
{P}   HACKING WORLD - YOUTUBE SUBSCRIBER TOOL
{A}------------------------------------------------
""")

# Subscriber Hack
def sub_hack():
    logo()
    channel = input(f"{C}[+] Enter YouTube Channel ID: ")

    print(f"\n{Y}[*] Connecting to YouTube Server...")
    time.sleep(2)

    print(f"{G}[✓] Channel Found: {channel}\n")
    time.sleep(1)

    subs = random.randint(500, 3000)
    for i in range(subs, subs+8000, random.randint(500, 1000)):
        print(f"{C}[+] Current Subscribers: {i}")
        time.sleep(0.8)

    print(f"\n{G}[✓] 14k Subscribers Sent Successfully!")
    print(f"{P}[*] Note: Open YouTube App to Check Subscribers (Prank!)")
    input(f"\n{C}Press Enter To Exit...")

# Start Tool
sub_hack()