import sys
input = sys.stdin.readline

li = []
 
for i in range(8):
    li.append(int(input()))

tmp = sorted(li, reverse=True)[:5]
res = []
for i in tmp:
    res.append(li.index(i)+1)
print(sum(tmp))
print(*sorted(res))