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
print(RED + "Made by Craft_Dani")
print(RESET)
input()
usrname = input("Enter your Username: ")
password = input("Enter your Password: ")
print(BLUE + "Logging in...")
print(RESET)
time.sleep(9)
print("Logged in as " + usrname)
print("Hello " + usrname + "!")
print("Welcome to Python OS 1.0")
print("")
print("")
print("")
print("")
print("")
print("What do you want to do?")
print("1: (COMING SOON) Calculator")
print("2: (beta mode) File Manager")
print("3: Web Browser")
print("4: (COMING SOON) Text Editor)")
print("5: About")
print("6: Help")
print("7: Credits")
print("8: Shut down computer")
print("9: Update")
print("10: Restart Computer")
print("11: Exit")
print("12: (COMING SOON) Terminal !!!:(select this option to boot into beta mode {if you dont know its an unreleased version with many MANYYY bugs})")
print("13: Windows 11 Installer")
print("14: Reinstall PyOS")


select1 = input("Select an option: ")
if select1 == "10":
  print("Restarting...")
  time.sleep(5)
  os.system("python3 main.py")
if select1 == "9":
  print("Updating...")
  time.sleep(5)
  os.system("python3 update.py")
if select1 == "8":
  print("Shutting down...")
  time.sleep(5)
  os.system("clear")
  os.system("python3 shutdown.py")
if select1 == "7":
  print("Credits:")
  print("Danicool20 - Creator of Python OS")
  print("")
if select1 == "6":
  print("Help:")
  print("")
  print("Calculator:")
  print("This is a calculator.")
  print("")
  print("File Manager:")
  print("This is a file manager.")
  print("")
  print("Terminal:")
  print("This is a terminal.")
  print("")
  print("Text Editor:")
  print("This is a text editor.")
  print("")
  print("About:")
  print("This is a about section.")
  print("")
  print("Help:")
  print("This is a help section.")
  print("")
  print("Credits:")
  print("This is a credits section.")
  print("")
  print("Shut down computer:")
  print("This is a shutdown section.")
  print("")
  print("Update:")
  print("This is a update section.")
  print("")
  print("Restart Computer:")
  print("This is a restart section.")
  print("")
  input()
  os.system("python3 main.py")
if select1 == "5":
  print("About:")
  print("This is a about section.")
  print("")
  print("Help:")
  print("This is a help section.")
  print("")
  print("Credits:")
  print("This is a credits section.")
  print("")
  print("Shut down computer:")
  print("This is a shutdown section.")
  print("")
  print("Update:")
  print("This is a update section")
  print()
  print("I am searching guys who can help me making this OS")
  input()
  os.system("python3 main.py")
if select1 == "4":
  print("Text Editor:")
  print("This is a text editor COMING SOON.")
  print("")
  input()
  os.system("python3 main.py")
if select1 == "3":
  print("Web Browser:")
  os.system("python3 apps/webbrowser.py")
  input()
  os.system("python3 main.py")
if select1 == "2":
  print("File Manager:")
  os.system("python3 apps/fileexplorer.py")
if select1 == "1":
  print("Calculator:")
  print("This is a calculator COMING SOON.")
  print("")
  input()
  os.system("python3 main.py")
if select1 == "":
  os.system("python3 deathscreen.py")
if select1 == "11":
  print("Exiting...")
  time.sleep(5)
  os.system("clear")
  exit()
if select1 == "12":
  print("Beta mode")
  print("y to start beta mode and x to leave")
  print("")
  inpo12 = input("ur choice")
  if inpo12 == "y":
    os.system("python3 debug-beta.py")
  else:
    os.system("py main.py")
  os.system("python3 main.py")
if select1 == "13":
  os.system("python3 windows11setup.py")#´
if select1 == "14":
  print("Reinstalling PyOS...")
  time.sleep(5)
  os.system("python3 installer.py")
