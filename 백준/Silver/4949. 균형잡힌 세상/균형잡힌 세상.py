import sys
input = sys.stdin.readline

while True:
    s = input()[:-1]
    if s == '.': break
    stack = [0]
    cur = stack[0]
    for i in s:
        if i == '(' or i == ')' or i == '[' or i == ']':
            stack.insert(0, i)
            if cur == '(' and i == ')':
                stack.pop(0)
                stack.pop(0)
            if cur == '[' and i == ']':
                stack.pop(0)
                stack.pop(0)
            cur = stack[0]
    if stack == [0]:
        print('yes')
    else: print('no')