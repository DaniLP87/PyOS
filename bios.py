import os
import time


print("BIOS of PythonOS")
print("----------------------")
print("What do you want to do?")
print("1: Update")
print("2: Exit")
print("")
select1 = input("Select a number: ")
if select1 == "1":
  print("Updating...")
  time.sleep(8)
  print("Update Complete!")
  print("")
  input()
  os.system("python3 update.py")
if select1 == "2":
  print("Exiting...")
  print("")
  os.system("exit")
