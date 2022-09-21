import sys
input = sys.stdin.readline

n, m, start_vertex = map(int, input().split())

connection = {i: list() for i in range(1, n+1)}

for _ in range(m):
  a, b = map(int, input().split())
  connection[a].append(b)
  connection[b].append(a)

def DFS(v=int, checked=[]):
  checked.append(v)
  tmp = sorted(connection[v])
  for i in tmp:
    if i not in checked:
      checked = DFS(i, checked)

  return checked


def BFS(start_vertex):
  # init
  checked = [start_vertex]
  queue = [start_vertex]
  while queue:
    v = queue.pop(0)
    tmp = sorted(connection[v])
    for i in tmp:
      if i not in checked:
        queue.append(i)
        checked.append(i)

  return checked

dfs_ = []
print(*DFS(start_vertex,dfs_))
print(*BFS(start_vertex))
# print(connection)