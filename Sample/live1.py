# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, B, C, D):
    DigitList = [A, B, C, D]

    DigitList.sort()
    print(DigitList)
    isfound = False
    for x in range(2400)[::-1]:
        temp = []
        i = x
        while (i >=0 and len(temp)<4):
            temp.append(i % 10)
            i = int(i / 10)
        temp.sort()
        print("temp",temp,x)
        if (temp == DigitList):
            y = x % 100
            z = y
            if (x % 100 > 59):
                print("111")
                z = str(y % 10) + str(y // 10)
                if (int(z) > 59):
                    print("222")
                    return "NOT POSSIBLE"
                else:
                    if (int(x / 100) < 10):
                        return "0" + str(int(x / 100)) + ":" + str(z)

                    return str(int(x / 100)) + ":" + str(z)
            else:
                if (int(x / 100) < 10):
                    return "0" + str(int(x / 100)) + ":" + str(z)
                return str(int(x / 100)) + ":" + str(z)

    if not isfound:
        return "NOT POSSIBLE"


res=solution(0, 0, 0, 0)
print(res)


