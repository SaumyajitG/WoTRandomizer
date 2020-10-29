import json
import requests
import random

# Loading all Tank Data
with open('/home/sam/code/Data/Tanks.json') as f:
    data=json.load(f)

rand=0
option =0

def trueRand():
    with open('/home/sam/code/api.json') as ap:
        request=json.load(ap)
    response=requests.post("https://api.random.org/json-rpc/2/invoke", headers={'Content-type': 'application/json'}, json=request)
    response=response.json()
    return response['result']['random']['data'][0]

def pseudoRand():
    return random.randint(1,37)


rand=trueRand()
print(rand)
print("--------------------------")
for i in data['Tank']:
    if int(i['id'])==rand:
        print(i['Name'])
        print("Tier " + i['Tier'])
        print(i['Country']+" "+i['Type']+" Tank")
