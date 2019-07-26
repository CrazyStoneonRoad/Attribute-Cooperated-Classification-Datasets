#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# -----------------------------------------
#
# Authorized by Zhang Yuanlin from
# the Key Laboratory of Spectral Imaging Technology CAS,
# Xi'an Institute of Optics and Precision Mechanics,
# Chinese Academy of Sciences, Xi'an 710119, China.
#
# -----------------------------------------
# count all words and show words that usually shows up.
# there is a threshold of the frequency.

import os,json,sys
print(sys.argv)

# read json
if len(sys.argv)>1:
    path = sys.argv[1]
else:
    path = './dataset.json'
#path = '/home/user3/DATA/CLASSIFICATION/RSICD-CLS/attribute/dataset_rsicd.json'

root = json.load(open(path,'r')) 

# dict for counting
Dict = {}

# count
for img in root['images']:
    for sent in img['sentences']:
        for word in sent['tokens']:
            word = word.lower()
            if word in Dict:
                Dict[word] = Dict[word] + 1
            else:
                Dict.update({word:1})
                # if | word='plane'
                # this can be written as | Dict.update(plane=1)
print(len(Dict))

# save the Dict
# outfile = '/home/user3/DATA/CLASSIFICATION/RSICD-CLS/attribute/count.txt'
outfile = './count.txt'
# sort by value
Dict = sorted(Dict.items(), key=lambda item:item[1], reverse=True)
lines = [cell[0]+'\t'+str(cell[1])+'\n' for cell in Dict]
#lines = [wd+'\t'+str(Dict[wd])+'\n' for wd in Dict]
with open(outfile,'w') as f:
    f.writelines(lines)
    
    
