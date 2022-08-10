import sys
input = sys.stdin.readline

s = input()[:-1]
m = int(input())
left = list(s)
right = []
for _ in range(m):
    inp = list(input().split())
    cmd = inp[0]
    if cmd == 'L':
        if left:
            w = left.pop()
            right.append(w)
    if cmd == 'D':
        if right:
            w = right.pop()
            left.append(w)
    if cmd == 'B':
        if left: # left가 비워져있지 않을 때 == 커서가 문장의 맨 앞
            left.pop()
    if cmd == 'P':
        left.append(inp[1])
    # print(left, right)
print(''.join(left+right[::-1]))

