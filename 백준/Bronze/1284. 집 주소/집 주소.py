import sys
input = sys.stdin.readline

while True:
    n = input().rstrip()
    if n == '0': break

    res = 2+len(n)-1
    for i in n:
        if i == '0': res += 4
        elif i == '1': res += 2
        else: res += 3
    
    print(res)
    res = 0
