import sys
input = sys.stdin.readline

# input
n = int(input())
p = list(map(int, input().split()))

p.sort()

cnt = 0
tmp = []
for i in p:
    tmp.append(i)
    cnt += sum(tmp)
print(cnt)