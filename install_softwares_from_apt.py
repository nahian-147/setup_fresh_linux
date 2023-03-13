import os
import json

to_be_installed = dict()

with open('install_python_packages.json') as file:
    to_be_installed = json.load(file)


for software in to_be_installed['apt_softwares']:
    os.system(f'sudo apt install {software}')
    