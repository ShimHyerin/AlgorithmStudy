import sys
input = sys.stdin.readline

n, m = map(int, input().split())

li = list(map(int, input().split()))

sumlist = []
tmp = 0
for i in li:
    tmp += i
    sumlist.append(tmp)

for _ in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    if a == 0: print(sumlist[b])
    else:
        print(sumlist[b]-sumlist[a-1])
