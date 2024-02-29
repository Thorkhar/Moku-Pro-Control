import json

with open('config.json', 'r') as file:
    settings = json.load(file)
    file.close()
