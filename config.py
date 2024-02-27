import json

with open('config.json', 'r') as file:
    settings = json.load(file)
    file.close()

settings['F_START'] = settings['F_START'] * settings['CHIRP_DURATION']
settings['F_STOP'] = settings['F_STOP'] * settings['CHIRP_DURATION']
