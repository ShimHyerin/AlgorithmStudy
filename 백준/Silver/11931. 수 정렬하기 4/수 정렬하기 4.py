import sys
input = sys.stdin.readline

# input
n = int(input())
li = []
for _ in range(n):
    li.append(int(input()))

li = sorted(li, reverse=True)
print(*li, sep='\n')