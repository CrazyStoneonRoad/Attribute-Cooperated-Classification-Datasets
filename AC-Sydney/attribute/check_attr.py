import json
import numpy as np

root = json.load(open('Attributes.json','r'))

for clsi in root: 
    for imgi in root[clsi]: 
        root[clsi][imgi] = [int(lt) for lt in root[clsi][imgi]] 

count=np.zeros(len(root[ list(root.keys())[0] ][ list(root[ list(root.keys())[0]].keys())[0] ]), dtype=np.int)

for clsi in root: 
    for imgi in root[clsi]: 
        count = count + np.array(root[clsi][imgi])

print(count)
