import sys
input = sys.stdin.readline

n, m = map(int, input().split())

connection = {i: list() for i in range(1, n+1)}
li = [v for v in range(1, n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  connection[a].append(b)
  connection[b].append(a)

# stack dfs
def DFS(v=int):
  checked = [v]
  stack = [v]

  while stack:
    vertex = stack.pop()
    for i in connection[vertex]:
      if i not in checked:
        checked.append(i)
        stack.append(i)
        li.pop(li.index(i))

  return checked


res = 0
while li:
  sv = li.pop(0)
  DFS(sv)
  res+=1

print(res)
# print(connection)