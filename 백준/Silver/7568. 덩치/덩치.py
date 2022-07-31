import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    x, y = map(int, input().split())
    lst.append((x, y))

rank = [1]*n
for i in range(n):
    x = lst[i][0]
    y = lst[i][1]
    cnt = 1
    for j in range(n):
        if j == i: continue
        if x < lst[j][0] and y < lst[j][1]:
            cnt += 1
    rank[i] = cnt

for i in rank:
    print(i, end=' ')
