s=input().strip()
count=0

def count1(p):
    k = 0
    n1 = len(p)
    while (k < int(n1 / 2)):
        if (p[k] == 0 and p[n1 - 1] == 1):
            k = k + 1
            n1 = n1 - 1

        else:
            return False

    return True

for i in range(len(s)+1):
    for j in range(i+1,len(s)+1):
        p=s[i:j]
        print(p)
        c=count1(p)
        if(c==True):
            count=count+1


print(count)