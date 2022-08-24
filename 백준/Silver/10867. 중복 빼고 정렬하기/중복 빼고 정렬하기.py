import sys
input = sys.stdin.readline

# input
n = int(input())
li = list(map(int, input().split()))

li = list(set(li))
print(*sorted(li))