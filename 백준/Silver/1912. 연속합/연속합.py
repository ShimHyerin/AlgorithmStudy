n = int(input())
numL= list(map(int, input().split()))
l = []
for i in range(n):
    l.append((0))

anw = -1001
for i in range(n):
    l[i] = max(l[i-1] + numL[i], numL[i])
    anw = max(anw, l[i])

print(anw)