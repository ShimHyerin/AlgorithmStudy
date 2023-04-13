import sys
input = sys.stdin.readline

n = int(input())

def sol():
    br = input().rstrip() # bracket string
    stack = []

    for i in br:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return 'NO'
    if stack:
        return 'NO'
    else:
        return 'YES'

for i in range(n):
    print(sol())
