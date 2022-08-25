import sys
input = sys.stdin.readline

# input
a, b = map(int, input().split())

tmp = a - (a*b/100)
print(1) if tmp < 100 else print(0)