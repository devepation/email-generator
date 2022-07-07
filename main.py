import os
import random
import string
import json
from time import sleep as wait

namesl = json.loads(open('names.json').read())

names = []
for name in namesl:
    name = name.lower()
    name_e = ''.join(random.choice(string.digits)+random.choice(string.digits)+random.choice(string.digits)+random.choice(string.digits))
    name = name + name_e
    names.append(name)
#print(names)
def doit():
    return random.choice(names) + "@yahoo.com"
    
while True:
    print(doit())
    wait(0.002)