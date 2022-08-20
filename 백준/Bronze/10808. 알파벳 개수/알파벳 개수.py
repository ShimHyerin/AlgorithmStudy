import sys
input = sys.stdin.readline

# input
s = input()[:-1]

alpha = 'abcdefghijklmnopqrstuvwxyz'
cnt = 0
for i in alpha:
    for j in s:
        if j == i:
            cnt +=1
    print(cnt, end = ' ')
    cnt = 0