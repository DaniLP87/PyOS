BLUE = "\033[1;34m"
RESET = "\033[0;0m"
RED = "\033[1;31m"
import os
import time

os.system("clear")
time.sleep(2)

print(BLUE+"  _____       _   _                    ____   _____   __   ___  ")
print(BLUE+" |  __ \     | | | |                  / __ \ / ____| /_ | / _ \ ")
print(BLUE+" | |__) |   _| |_| |__   ___  _ __   | |  | | (___    | || | | |")
print(BLUE+" |  ___/ | | | __| '_ \ / _ \| '_ \  | |  | |\___ \   | || | | |")
print(BLUE+" | |   | |_| | |_| | | | (_) | | | | | |__| |____) |  | || |_| |")
print(BLUE+" |_|    \__, |\__|_| |_|\___/|_| |_|  \____/|_____/   |_(_)___/ ")
print(BLUE+"         __/ |                                                  ")
print(BLUE + "        |___/                                                   ")
print("")
print(RED + "Made By Craft_Dani")
print(RESET + "")
input()

print("Hello User, welcome to the Python os installer!")
print("Which version do you want to install?")
print("1: Exit installation")
print("2: School Version")
print("3: Beta Version")
print("4: Normal Version")
print("")
select1 = input("Select a number: ")
if select1 == "1":
  print("Exiting Installation...")
  exit()
if select1 == "3":
  print("Beta Version COMING SOON")
  print("")
  input()
  os.system("python3 installer.py")
if select1 == "2":
  print("School Version COMING SOON")
  print("")
  input()
  os.system("python3 installer.py")
if select1 == "4":
  print("installing normal version...")
  # github copyability
  
  time.sleep(3)
  print("Normal Version installed! do you want to enter the OS? (y/n)")
  print("")
  select2 = input("Select an option: ")
  if select2 == "y":
    print("Entering OS...")
    print("")
    os.system("python3 main.py")
  if select2 == "n":
    print("Exiting Installer...")
    print("")
    os.system("python3 bios.py")
