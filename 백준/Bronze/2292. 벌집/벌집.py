import sys
input = sys.stdin.readline

N = int(input())
cnt = 1
max_num = 1
while True:
    if N <= max_num: break
    max_num += cnt*6
    cnt += 1
print(cnt)