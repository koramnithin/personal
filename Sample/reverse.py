def reverse3(s):
    l = s.split()
    p=''
    for i in l:
        p += ' '+i[::-1]
    print(p)
    return p

def reverseStr(s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    s = list(s)
    for i in xrange(0, len(s), 2 * k):
        s[i:i + k] = reversed(s[i:i + k])
    return "".join(s)

print(reverseStr("abcdefg",2))