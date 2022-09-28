import sys
input = sys.stdin.readline

n = int(input())
li = []
for i in range(n):
    name, d, m, y = input().split()
    li.append([name, int(d), int(m), int(y)])

li = sorted(li, key=lambda x: (x[3], x[2], x[1]), reverse=True)
print(li[0][0])
print(li[-1][0])