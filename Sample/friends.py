#!/bin/python3

import sys


t = int(input().strip())
dict1={}

for a0 in range(t):
    n,m = input().strip().split(' ')
    n,m = [int(n),int(m)]
    total = 0
    for i in range(1,n+1):
        dict1[i]=[i]

    for a1 in range(m):
        x,y = input().strip().split(' ')
        x,y = [int(x),int(y)]
        # your code goes here
        sum = 0
        # if(x not in dict1[y]):
        #     dict1[y].append(x)
        # if y not in dict1[x]:
        #     dict1[x].append(y)
        for i in dict1[x]:
            for j in dict1[i]:
                if i not in dict1[i]:
                    dict1[j].append(i)
        for i in dict1[y]:
            for j in dict1[i]:
                if i not in dict1[i]:
                    dict1[i].append(j)
        for i in range(1,n+1):
            sum=sum+(len(set(dict1[i]))-1)
        print(sum)
        total+=sum
    print(total)



