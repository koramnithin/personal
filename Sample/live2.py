# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    B = []
    B=list(A)
    B.sort()
    min = []
    count = 0
    j = 0
    i = 0
    # for i in range(len(A)):
    while (i < len(A)):
        if (A[j] == B[i]):
            count = i - j
            print(i,j,count)
            if (count > 0):
                min.append(count + 1)
                j = i
            i = i + 1
            j = j + 1
        elif (A[j] != B[i]):
            i = i + 1

    print(min)
    if (len(min) == 0):
        return 0
    else:
        min.sort()
        return min[0]

res=solution([1, 2, 6, 5, 5, 8, 9,12,10,11,13,14,20,19,18,21,22])
print(res)