n = int(input())

ans = 1000001
for i in range(1, n):
    tmp = str(n-i)
    m = n-i
    for j in tmp:
        m += int(j)
    if m == n:
        ans = min(ans, n-i)

if ans == 1000001: print(0)
else: print(ans)
