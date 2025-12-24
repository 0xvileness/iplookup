import requests
import sys

print()
print(" ▪   ▄▄▄·          .▄▄ · ▪   ▐ ▄ ▄▄▄▄▄    ")
print(" ██ ▐█ ▄█    ▪     ▐█ ▀. ██ •█▌▐█•██    ")  
print(" ▐█· ██▀·     ▄█▀▄ ▄▀▀▀█▄▐█·▐█▐▐▌ ▐█.▪   ")
print(" ▐█▌▐█▪·•    ▐█▌.▐▌▐█▄▪▐█▐█▌██▐█▌ ▐█▌·  ")  
print(" ▀▀▀.▀        ▀█▄▀▪ ▀▀▀▀ ▀▀▀▀▀ █▪ ▀▀▀   ")  
print("          Made By @0xvileness  ")                                                                   
print()


ip_address = input("Enter an ip-address: ")
response = requests.get("http://ip-api.com/json/" + ip_address)

print(response.json())
