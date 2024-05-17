import json
import os
import secrets
import string
import requests
from time import sleep


class wifihack():
    logo = ("""\033[1;32m
            ██╗    ██╗██╗███████╗██╗    ██╗  ██╗ █████╗  ██████╗██╗  ██╗
            ██║    ██║██║██╔════╝██║    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝
            ██║ █╗ ██║██║█████╗  ██║    ███████║███████║██║     █████╔╝ 
            ██║███╗██║██║██╔══╝  ██║    ██╔══██║██╔══██║██║     ██╔═██╗ 
            ╚███╔███╔╝██║██║     ██║    ██║  ██║██║  ██║╚██████╗██║  ██╗
             ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                                                            

    \033[1;32m═════════════════════════════════════════════
                \033[1;31m| \033[1;32mVERISION\033[1;31m => \033[1;32m1.0 \033[1;31m| \033[1;32m
    \033[1;32m═════════════════════════════════════════════
    \033[1;31m[\033[1;32m+\033[1;31m]\033[1;32m Modify \033[1;31m: \033[1;32m Mr.Cyb3rgh0st
    \033[1;31m[\033[1;32m+\033[1;31m]\033[1;32m Github \033[1;31m: \033[1;32m Mr-Cyb3rgh0st
    \033[1;31m[\033[1;32m+\033[1;31m]\033[1;32m TOOL    \033[1;31m: \033[1;32m  Wifi Hacking Tool
    \033[1;31m[\033[1;32m+\033[1;31m]\033[1;32m Telegram  \033[1;31m: \033[1;32m @Mr.Cyb3rgh0st
    \033[1;32m═════════════════════════════════════════════""")

    def __init__(self):
        self.clear()
        print(self.logo)
        self.menu()
        
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

                                                    # MENU BAR
    def menu(self):    
        # self.clear() 
        print(' \033[1;31m[\033[1;32m1\033[1;31m]\033[1;32m Scan All Wifi Networks \033[1;31m')
        print(' \033[1;31m[\033[1;32m2\033[1;31m]\033[1;32m Pixie Dust attack on a specified BSSID \033[1;31m')
        print(' \033[1;31m[\033[1;32m3\033[1;31m]\033[1;32m WPS bruteforce with the specified first half of the PIN \033[1;31m')
        print(' \033[1;31m[\033[1;32m4\033[1;31m]\033[1;32m Start WPS push button connection \033[1;31m')
        print(' \033[1;31m[\033[1;32m5\033[1;31m]\033[1;32m Exit \033[1;31m')
        
        self.option=input(' \033[1;31m[\033[1;32m+\033[1;31m]\033[1;32m Choose Your Option \033[1;31m ==>  ')

        if self.option=='1':
            os.system('sudo python Cyb3rgh0st.py -i wlan0 --iface-down -K')
        elif self.option=='2':
            BSSID=input(' \033[1;31m[\033[1;32m*\033[1;31m]\033[1;32m Enter Network BSSID \033[1;31m ==>  ')
            os.system(f'sudo python3 Cyb3rgh0st.py -i wlan0 -b {BSSID} -K')
        elif self.option=='3':
            BSSID=input(' \033[1;31m[\033[1;32m*\033[1;31m]\033[1;32m Enter Network BSSID \033[1;31m ==>  ')
            pin=input(' \033[1;31m[\033[1;32m*\033[1;31m]\033[1;32m Enter the first half of the PIN \033[1;31m ==>  ')
            os.system(f'sudo python3 Cyb3rgh0st.py -i wlan0 -b {BSSID} -B -p {pin}')
        elif self.option=='4':
            os.system('sudo python3 Cyb3rgh0st.py -i wlan0 --pbc')
        elif self.option=='5':
            exit()
        else:
            print(' \033[1;31m[\033[1;32m!\033[1;31m]\033[1;32m Invalid Option \033[1;31m')
            sleep(1)
            self.clear()
            print(self.logo)
            self.menu()
boom=wifihack()
