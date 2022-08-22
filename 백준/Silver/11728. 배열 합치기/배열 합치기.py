import sys
input = sys.stdin.readline

# input
n, m = map(int, input().split())

li = []
a = list(map(int, input().split()))
b = list(map(int, input().split()))
li = a+b
li.sort()
print(*li)