import os
os.system("clear")

RED = "\033[31m"
RESET = "\033[38;2;255;255;255m"
# deathscreen
print(RED+"                ")
print(RED+"             _  ")
print(RED+"           .' ) ")
print(RED+" ,.--.    / .'  ")
print(RED+"//    \  / /    ")
print(RED+"\\    / / /     ")
print(RED+" `'--' . '      ")
print(RED+" ,.--. | |      ")
print(RED+"//    \' '      ")
print(RED+"\\    / \ \     ")
print(RED+" `'--'   \ \    ")
print(RED+"          \ '.  ")
print(RED+"           '._) ")
print(RED+"")
print("An fatal error occured while running the OS")
print("Press Enter to Restart The Computer (it will help to start main.py again)")
input()
os.system("python3 main.py")
