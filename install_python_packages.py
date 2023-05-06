import os
import json

to_be_installed = dict()

with open('softwares.json') as file:
    to_be_installed = json.load(file)

for package in to_be_installed['package_list']:
    os.system(f'python3 -m pip install {package}')
    