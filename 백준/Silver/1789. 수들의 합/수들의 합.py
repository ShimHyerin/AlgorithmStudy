import sys
input = sys.stdin.readline

s = int(input())
tmp = 0
n = 0
while tmp <= s:
    n += 1
    tmp += n

print(n-1)