import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = {i: list() for i in range(1, n+1)}

for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def DFS(v, li):
  li.append(v)
  for i in graph[v]:
    if i not in li:
      li = DFS(i, li)
  
  return li

li = []
print(len(DFS(1, li))-1)
# print(graph)

