import sys
input = sys.stdin.readline

n, k = map(int, input().split())

cnt = 1
q = [i for i in range(1, n+1)][::-1]
q_ = []
ans = []
while True:
    if not q: 
        q = q_[::-1]
        q_ = []
    if cnt == k:
        ans.append(q.pop())
        cnt = 0
    else:
        q_.append(q.pop())
    
    cnt += 1
    if len(ans) == n: break

print('<', end='')
print(*ans, sep=', ', end='')
print('>')