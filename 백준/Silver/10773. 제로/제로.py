import sys
input = sys.stdin.readline

n = int(input())

res = []
for i in range(n):
    k = int(input())
    if k == 0 and res:
        res.pop()
    else:
        res.append(k)

print(sum(res))