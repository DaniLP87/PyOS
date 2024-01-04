import os
import time
import sys
import subprocess
import json
import shutil

os.system("clear")
time.sleep(1)

BLUE = "\033[34m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
WHITE = "\033[37m"
END = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
REVERSE = "\033[7m"
RESET = "\033[0m"


print(BLUE+"  _____       _   _                    ____   _____   __   ___  ")
print(BLUE+" |  __ \     | | | |                  / __ \ / ____| /_ | / _ \ ")
print(BLUE+" | |__) |   _| |_| |__   ___  _ __   | |  | | (___    | || | | |")
print(BLUE+" |  ___/ | | | __| '_ \ / _ \| '_ \  | |  | |\___ \   | || | | |")
print(BLUE+" | |   | |_| | |_| | | | (_) | | | | | |__| |____) |  | || |_| |")
print(BLUE+" |_|    \__, |\__|_| |_|\___/|_| |_|  \____/|_____/   |_(_)___/ ")
print(BLUE+"         __/ |                                                  ")
print(BLUE + "        |___/                                                   ")
print(BLUE + "")
print(YELLOW + "Beta Mode -- Alpha 0.1")
print(RESET)
input()
usrname = input("Enter your Betakey: ")
print(BLUE + "Going into Betamode...")
print(RESET)
time.sleep(9)
print("Logged in as user")
print("Hello user!")
print("Welcome to Python OS 1.0 BETA MODE")
print("")
print("")
print("")
print("")
print("")
print("What do you want to do?")
print("1: ")
print("2: ")
print("3: Web Browser")
print("4: ")
print("5: Reboot into Normal Mode")
print("6: Help")
print("7: Credits")
print("8: Shut down computer")
print("9: Update")
print("10: Restart Computer")
print("11: Exit")
print("12: Enter Shell")
print("13: ")
print("14: Reinstall PyOS")


select1 = input("Select an option: ")
if select1 == "10":
  print("Restarting...")
  time.sleep(5)
  os.system("python3 debug-beta.py")
if select1 == "9":
  print("Updating...")
  time.sleep(5)
  os.system("python3 debug-beta.py")
if select1 == "8":
  print("Shutting down...")
  time.sleep(5)
  os.system("clear")
  os.system("python3 shutdown-beta.py")
if select1 == "7":
  print("Credits:")
  print("DEACTIVATED IN BETAMODE")
  print("")
if select1 == "6":
  print("Help:")
  print("")
  print("DEACTIVATED IN BETAMODE")
  input()
  os.system("python3 main.py")
if select1 == "5":
  print("NOT HERT")
  os.system("python3 betacrash.py")
if select1 == "12":
    os.system("clear")
    sh = input("$ ")
    os.system(sh)