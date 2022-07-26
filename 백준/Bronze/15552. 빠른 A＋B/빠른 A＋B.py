import sys
n = int(input())
for i in range(n):
    a, b = sys.stdin.readline().rsplit()
    print(int(a) + int(b))