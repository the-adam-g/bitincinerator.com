import os
import secrets
from random import randint

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
print(contentslength)
file.close()
file = open(newpath, "wb")
file.truncate()
file.write(secrets.token_bytes(contentslength))
file.close()
os.remove(newpath)
print("File has been successfully overwritten and deleted.")
print("Thank you for using BitIncinerator")