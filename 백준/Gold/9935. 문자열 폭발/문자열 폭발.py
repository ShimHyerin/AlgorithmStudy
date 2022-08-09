import sys
input = sys.stdin.readline

s = input()[:-1]
x = input()[:-1]
len_x = len(x)

stack = [] # init stack

for i in s:
    stack.append(i) # stack push
    if i == x[-1] and x == ''.join(stack[len(stack)-len_x:]):
        for _ in range(len_x):
            stack.pop()


s = ''.join(stack)


if s == '': print('FRULA')
else: print(s)