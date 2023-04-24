import sys
input = sys.stdin.readline

h, m, s = map(int, input().split())
d = int(input())

a = d//60
b = d%60

if s + b >= 60:
    m += (s+b) // 60
    s = (s+b) % 60
else:
    s += b

if m + a >= 60:
    h += (m+a) // 60
    m = (m+a) % 60
else:
    m += a

if h >= 24:
    h = h %24

print(h, m, s)