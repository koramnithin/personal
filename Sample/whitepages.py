import sys
def dungeoneeing(arr):
    i=0
    j=1
    res="0"
    length=len(arr)

    while j < length:
        #min of length of array as it is the maximum position steps
        # to reach end of array and current value in arr[i]
        endj = min(arr[i] + i + 1, length)
        while j < endj:
            if arr[j] + j > arr[i] + i:
                i = j
            j += 1
        if(i == 0):
            # No solution as the step cannot be 0
            return "failure"
        else:
            # when last jump can not read current i,
            # append string with current index i.e "i"
            res+=", "+str(i)
    return res+", out"


if __name__=="__main__":
    arr = sys.stdin.readlines()
    for i in range(len(arr)):
        try:
            arr[i] = int(arr[i].split('\n')[0])
        except ValueError:
            print("failure")
            exit(0)
    print(dungeoneeing(arr))