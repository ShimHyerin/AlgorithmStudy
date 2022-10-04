import sys
input = sys.stdin.readline

n, m = map(int, input().split())

map = [list(input().rstrip()) for _ in range(n)]
check = [[0]*m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = [(0, 0)]
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < m and map[nx][ny] == '1' and check[nx][ny] == 0:
                check[nx][ny] = check[x][y] + 1
                q.append((nx, ny))
    return check[n-1][m-1]
    
print(bfs()+1)
