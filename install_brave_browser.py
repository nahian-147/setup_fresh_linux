import os
import json

to_be_installed = None

os.system('sudo apt update')
os.system('sudo apt upgrade -y')

with open('softwares.json') as file:
    to_be_installed = json.load(file)
    
for command in to_be_installed["brave_browser"]:
    os.system(command)
