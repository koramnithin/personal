def  improbabilityCalculator(coordinates, remove):
    res=""
    res = tempFun(coordinates,remove,res)
    return res
    pass


def tempFun(s,rem,res):
    length=len(s)
    if rem == 0:
        res+=s
        return res
    if rem>length:
        res+=""
        return "0"
    if length == 0:
        return res
    else:
        minIndex=0
        for i in range(1,rem+1):
            if s[i]<s[minIndex]:
                minIndex=i
        temp=s[minIndex]
        res+=temp
        new_res=s[minIndex+1:]
        res = tempFun(new_res,rem-minIndex,res)
        return res
