import sys
input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    command = input().split()
    if command[0] == 'push':
        stack.insert(0, command[1])
    if command[0] == 'pop':
        if stack:
            print(stack[0])
            stack.pop(0)
        else: print(-1)
    if command[0] == 'size':
        print(len(stack))
    if command[0] == 'empty':
        if stack: print(0)
        else: print(1)
    if command[0] == 'top':
        if stack: print(stack[0])
        else: print(-1)