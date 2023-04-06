import os
import json

to_be_installed = None

with open('softwares.json') as file:
    to_be_installed = json.load(file)


os.system('sudo apt update')
os.system('sudo apt upgrade -y')
for software in to_be_installed['apt_softwares']:
    os.system(f'sudo apt install {software} -y')
    
for command in to_be_installed["mongodb"]:
    os.system(command)
    
