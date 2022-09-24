import sys
input = sys.stdin.readline

n = int(input())

li = []
d ={i:list() for i in range(n)}
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 1: d[i].append(j)

    li.append(line)

def dfs(v, i, checked):
    for j in d[v]:
        if j not in checked:
            checked.append(j)
            li[i][j] = 1
            dfs(j, i, checked)

    return li[i]

dfs_ = []
for i in range(n):
    print(*dfs(i, i, dfs_))
    dfs_ = []
