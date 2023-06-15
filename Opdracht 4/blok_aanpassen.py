import json

# het 'grass_block.json' bestand stond niet bij de opdracht dus ik heb er zelf maar een gemaakt
with open('grass_block.json', 'r') as file: 
    json_data = json.load(file)

json_data['name'] = "Snow Block"
json_data['pos_Y'] += 55
json_data['pos_Z'] *= 3
json_data['snow'] = True

json_data = json.dumps(json_data)

with open('snow_block.json', 'w') as file:
    file.write(json_data)