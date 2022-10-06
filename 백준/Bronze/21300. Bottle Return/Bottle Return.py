import sys
input = sys.stdin.readline

li = list(map(int, input().split()))
cnt = 0
for i in li:
    cnt += i*5
print(cnt)