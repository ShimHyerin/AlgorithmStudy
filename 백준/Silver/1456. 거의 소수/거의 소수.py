import sys
input = sys.stdin.readline

a, b = map(int, input().split())
n = 10**7+5
lst = [False, False] + [True]*(n) # 0, 1 -> False

cnt =0

for i in range(2, n):
    if lst[i]:
        N = 2
        tmp = i**N
        while tmp <= b:
            if tmp >= a:
                cnt += 1
            N += 1
            tmp = i**N
        for j in range(2*i, n-1, i):
            lst[j] = False
print(cnt)