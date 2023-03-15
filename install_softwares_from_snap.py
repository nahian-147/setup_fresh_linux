import os
import json

to_be_installed = dict()

with open('softwares.json') as file:
    to_be_installed = json.load(file)


for software in to_be_installed['snap_softwares']:
    os.system(f'sudo snap install {software}')
    