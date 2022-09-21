import sys
input = sys.stdin.readline

n, m = map(int, input().split())

connection = {i: list() for i in range(1, n+1)}
kevin_bacon = [0]*n

for _ in range(m):
  a, b = map(int, input().split())
  connection[a].append(b)
  connection[b].append(a)

def BFS(start_user):
  # init
  checked = [start_user]
  queue = [start_user]
  kevin = [0]*n
  while queue:
    user = queue.pop(0)
    for i in connection[user]:
      # cnt+= 1
      if i not in checked:
        queue.append(i)
        checked.append(i)
        kevin[i-1] = kevin[user-1]+1

  return sum(kevin)

for i in range(1,n+1):
  kevin_bacon[i-1] = BFS(i)
  
print(kevin_bacon.index(min(kevin_bacon))+1)