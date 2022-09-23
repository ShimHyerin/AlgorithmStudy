import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) # 재귀 제한 강제 변경


t = int(input())

for _ in range(t):
  # m = 가로길이 n = 세로 길이 k = 배추개수
  m, n, k = map(int, input().split())

  # init 
  field = []
  for _ in range(n):
    field.append([0]*m)

  for _ in range(k):
    a, b = map(int, input().split())
    field[b][a] = 1

  cnt = 0

  # dfs
  def DFS(x, y):
    # exception
    if x <= -1 or x >= n or y <= -1 or y >= m:
      return 0

    if field[x][y]:
      field[x][y] = 0

      DFS(x-1, y)
      DFS(x+1, y)
      DFS(x, y-1)
      DFS(x, y+1)

      return 1
    
    else: return 0

  for i in range(n):
    for j in range(m):
      cnt += DFS(i, j)
  print(cnt)
