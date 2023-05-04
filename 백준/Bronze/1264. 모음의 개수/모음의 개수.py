import sys
input = sys.stdin.readline

li = ['a', 'e', 'i', 'o', 'u']
while True:
    s = input().rstrip().lower()
    if s == '#': break
    cnt = 0
    for i in s:
        if i in li: cnt += 1
    print(cnt)