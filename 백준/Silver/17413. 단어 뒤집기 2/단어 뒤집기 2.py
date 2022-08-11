import sys
input = sys.stdin.readline

s = list(input()[:-1])
ans = ''
tg = 0
stack = []

for i in range(len(s)):
    if s[i] == '<': # tag open
        tg = 1
        ans += ''.join(stack)[::-1]
        stack = []
    if tg == 0:
        stack.append(s[i])
    else:
        ans += s[i]

    if tg == 0 and s[i] == ' ': # space
        stack.pop()
        ans += ''.join(stack)[::-1] + ' '
        stack = []

    if s[i] == '>': # tag close
        tg = 0

if stack:
    ans += ''.join(stack)[::-1]

print(ans)