import sys
input = sys.stdin.readline

n, k = map(int, input().split())

lst = [False, False] + [True]*(n-1) # 0, 1 -> False
cnt = 0

for i in range(2, n+1):
    if lst[i]:
        for j in range(i, n+1, i): # range(start, stop, step)
            if lst[j]:
                lst[j] = False
                cnt += 1
                if cnt == k:
                    print(j)
                    break
