#!/usr/bin/env python3

import json

with open('nboard.json', 'r') as file:
    data = json.load(file)

print(len(data))

data = {k:v for k, v in data.items() if v is not " "}

print(len(data))

with open('nboard.json', 'w') as file:
    json.dump(data, file)

