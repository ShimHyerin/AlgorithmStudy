import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]

def check(mid):
    cnt = 0
    for i in range(k):
        cnt += lan[i] // mid
    return cnt >= n

lo = 0
hi = int(2e31)-1

while lo+1 < hi:
    mid = (lo+hi) // 2
    if check(mid): lo = mid
    else: hi = mid

print(lo)