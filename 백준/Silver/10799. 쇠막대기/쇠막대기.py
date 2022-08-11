import sys
input = sys.stdin.readline

s = list(input()[:-1])
cnt = 0

tg = 0
stack = []
for i in range(len(s)):
    if s[i] == ')':
        stack.pop()
        if stack:
            if s[i-1] == '(':
                cnt += len(stack)
            elif tg == 1:
                cnt += 1
        else:
            if tg == 1:
                cnt += 1
                tg = 0
    else: stack.append(s[i])
    if len(stack) > 1: tg = 1
if stack: cnt += len(stack)
print(cnt)