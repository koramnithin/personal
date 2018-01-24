import json

f = open('C:\Users\keert\Documents\codecomments/sample-1M.jsonl','r')
heads = []
desc = []

for i in f.readlines():
    my_json = json.loads(i)
    heads.append(my_json['title'])
    desc.append(my_json['content'])
    # print heads,desc
f.close()

import pickle
mytup = (heads,desc,None)
pickle.dump( mytup, open( "data.pkl", "wb" ))

