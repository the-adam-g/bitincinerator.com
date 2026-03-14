import os
import secrets
from random import randint

banner = r'''
    ____  _ __     ____           _                       __                                    
   / __ )(_) /_   /  _/___  _____(_)___  ___  _________ _/ /_____  _____    _________  ____ ___ 
  / __  / / __/   / // __ \/ ___/ / __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/   / ___/ __ \/ __ `__ \
 / /_/ / / /_   _/ // / / / /__/ / / / /  __/ /  / /_/ / /_/ /_/ / /     _/ /__/ /_/ / / / / / /
/_____/_/\__/  /___/_/ /_/\___/_/_/ /_/\___/_/   \__,_/\__/\____/_/     (_)___/\____/_/ /_/ /_/ 
                                                                                                    
'''
print(banner)
while True:
    try:
        mode = int(input("Enter an integer for your mode (1 - Overwrite and delete, 2 - Overwrite and keep): "))
        break 
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
path = input("Enter the path of your file\n")
path = path.strip('"')
root, name = os.path.split(path)
try:
    newpath = root + "\\incinerated.txt"
    os.rename(path, newpath)
except:
    newpath = root + "\\incinerated.txt"
    os.rename(path, newpath)
file = open(newpath, "rb")
contentslength = len(file.read())
file.close()
file = open(newpath, "wb")
file.truncate()
file.write(secrets.token_bytes(contentslength))
file.close()
match mode:
    case 1:
        os.remove(newpath)
        print("File has been successfully overwritten and deleted.")
        print("Thank you for using BitIncinerator")
        input("Press enter to close.")
    case 2:
        print("File has been successfully overwritten.")
        print("Thank you for using BitIncinerator")
        input("Press enter to close.")