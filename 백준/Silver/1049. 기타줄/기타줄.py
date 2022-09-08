import sys
input = sys.stdin.readline

n, m = map(int, input().split())
set_, single_ = 1001, 1001
# ans = 999999999999
for _ in range(m):
  a, b = map(int, input().split())
  set_, single_ = min(a, set_), min(b, single_)


tmp = n//6
ans = min(set_*(tmp+1), set_*tmp+(n%6)*single_, single_*n)
print(ans)