import subprocess
from colorama import Fore
from pyfiglet import Figlet
PURPLE = "\033[0;35m"
def wifihack_banner():
    f = Figlet()
    print(PURPLE+f.renderText('Mr.Cyb3rgh0st'))
    print(Fore.LIGHTCYAN_EX+"====================> Wifi Hack < ====================")

cmd = ["sudo", "python", "wifi.py", "-i", "wlp2s0","--iface-down","-K"]
wifihack_banner()
subprocess.run(cmd)

