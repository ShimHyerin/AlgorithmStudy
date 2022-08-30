import sys
input = sys.stdin.readline

n = int(input())
H = [int(input()) for _ in range(n)]

stack = []
cnt = 0
for i in range(1, len(H)+1):
    tmp = 0
    while stack and H[i-1] >= H[stack[-1]-1]:
        if tmp > 0:
            last_ = stack.pop()
            if H[last-1] != H[last_-1]:
                cnt += i-last_-1
                # print(cnt)
            last = last_
            tmp += 1
        else:
            cnt += tmp
            tmp += 1
            last = stack.pop()
        # cnt += i - stack.pop() - 1
        # print('d', cnt, H[last-1])
    stack.append(i)

for i in stack:
    cnt += (len(H))-i
print(cnt)