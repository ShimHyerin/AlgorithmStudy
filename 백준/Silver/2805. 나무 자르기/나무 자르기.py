import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree_h = list(map(int, input().split()))

def check(x):
    s = 0
    for i in range(n):
        if tree_h[i] > x: s += (tree_h[i] - x) 
    return s >= m

lo = 0
hi = int(1e9)

while lo+1 < hi:
    mid = (lo+hi) // 2
    if check(mid): lo = mid
    else: hi = mid

print(lo)