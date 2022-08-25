import sys
input = sys.stdin.readline

# input
n = int(input())

for _ in range(n):
    print('yes') if 6 <= len(input().strip()) <= 9 else print('no')