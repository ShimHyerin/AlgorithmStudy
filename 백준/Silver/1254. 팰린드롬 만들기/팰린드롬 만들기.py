import sys
input = sys.stdin.readline

# input
s = input()[:-1]

if s == s[::-1]: print(len(s))
else:
    cnt = 1
    for i in range(1, len(s)):
        tmp = s[i:]
        if tmp == tmp[::-1]: break
        else: cnt += 1
    print(len(s)+cnt)
