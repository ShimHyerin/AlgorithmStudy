import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())

# init
g = {i:list() for i in range(1, n+1)}
for i in range(1, m+1):
  a_, b_ = map(int, input().split())
  g[a_].append(b_)
  g[b_].append(a_)

# solution
def sol(v, connect, cnt):
  connect.append(v)
  if v == b: 
    print(cnt)
    exit()
  else:
    cnt += 1
    for i in g[v]:
      if i not in connect:
        connect = sol(i, connect, cnt)

    return connect

connect = []
sol(a, connect, 0)
print(-1)
