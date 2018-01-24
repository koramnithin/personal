#!/usr/bin/env python
import distsim
word_to_vec_dict = distsim.load_word2vec("nyt_word2vec.4k")
# word_to_vec_dict = distsim.load_word2vec("glove.6B.50d.txt")
f = open("word-test.v3.txt","r")
count_1 = 0
count_5 = 0
count_10 = 0
n=0
lines = f.readlines()
incrct = []
crct = []
cat = ''
cat_arr = []
flag = False
crct_flag = False
for line in lines[1:]:
    if line.strip() != '':
        l=line.strip().split()
        if l[0]==':':
            if not flag and n != 0 and crct_flag:
                print cat + ' :', (count_1 * 1.0 / n) * 100, (count_5 * 1.0 / n) * 100, (
                                                                                        count_10 * 1.0 / n) * 100
                count_1 = 0
                count_5 = 0
                count_10 = 0
                n = 0
            cat = str(l[1])
            cat_arr.append(cat)
            flag = True
            crct_flag = False
        else:
            n+=1
            flag = False
            temp = []
            s = []
            for i in l:
                if i.strip() != '':
                    temp.append(word_to_vec_dict[i])
                    s.append(i)
            ret = distsim.show_nearest(word_to_vec_dict,temp[0]-temp[1]+temp[3],set([s[0],s[1],s[3]]),distsim.cossim_dense)
            unzip = zip(*ret)

            if s[2] in list(unzip[0])[:1]:
                count_1 +=1

            if s[2] in list(unzip[0])[:5]:
                count_5 +=1

            if s[2] in list(unzip[0])[:10]:
                count_10 +=1
            else:
                if not crct_flag:
                    incrct.append(s[0]+' '+s[1]+' '+unzip[0][0]+' '+s[3])
                    crct.append(s[0]+' '+s[1]+' '+s[2]+' '+s[3])
                    crct_flag = True

if n!=0:
    print cat + ' :', (count_1 * 1.0 / n) * 100, (count_5 * 1.0 / n) * 100, (count_10 * 1.0 / n) * 100
    count_1 = 0
    count_5 = 0
    count_10 = 0
    n=0
f.close()

for i in range(len(incrct)):
    print cat_arr[i]+' :'
    print 'Expected ->'+crct[i]
    print 'Actual ->'+incrct[i]
