def  reverseButPreserveWhitespace(reverseMe):
    length=len(reverseMe)
    res=[' ']*length
    wordList=reverseMe.split(' ')

    print(wordList)
    for i in range(len(wordList)):
        if(len(wordList[i])>0):
            index=reverseMe.index(wordList[i][0])
            temp=wordList[i][::-1]
            print(temp)
            # p=index
            for j in temp:
                res[index]=j
                index+=1
    return str(res)
print(reverseButPreserveWhitespace("Secret Message     test"))