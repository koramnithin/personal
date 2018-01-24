import codecs
f = codecs.open('C:\Users\keert\Documents\codecomments/coherence_raw_data.txt','r',"utf-8")
f1 = codecs.open('C:\Users\keert\Documents\codecomments/jfree1.txt','r',"utf-8")
f2 = codecs.open('C:\Users\keert\Documents\codecomments/jfree2.txt','r',"utf-8")
f3 = codecs.open('C:\Users\keert\Documents\codecomments/jhot.txt','r',"utf-8")
all = f.readlines() + f1.readlines() + f2.readlines() + f3.readlines()
data = []
heads = []
desc = []
head_str = ''
desc_str = ''
flag = False
fl = False
for i in all:
    if i.strip() == '':
        continue
    if i.strip() == '###':
        heads.append(head_str)
        desc.append(desc_str[2:]+'}')
        head_str = ''
        desc_str = ''
        fl = False
    if i[0] == '/':
        flag = True
        head_str += i.strip()[4:] + ' '
    if flag and i[0]==' ' :
        if i.strip()[-1] == '/':
            flag = False
            fl = True
        else:
            head_str += i.strip()[2:]+' '
    if fl and not flag and i[0]==' ':
        desc_str += i.strip()+' '
f.close()

w1 = codecs.open('comments.txt','w',"utf-8")
w2 = codecs.open('code.txt','w',"utf-8")
for i in range(len(heads)):
    w1.write(heads[i]+'\n')
    w2.write(desc[i]+'\n')
w1.close()
w2.close()

import pickle
mytup = (heads,desc,None)
pickle.dump( mytup, open( "code_comments.pkl", "wb" ))

