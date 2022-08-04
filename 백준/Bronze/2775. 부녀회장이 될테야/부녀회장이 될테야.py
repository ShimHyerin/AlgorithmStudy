import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input()) # k층
    n = int(input()) # n호

    p = [i for i in range(1, n+1)] # 0층
    for i in range(1, k+1):
        tmp = [0]*n
        for j in range(1, n+1):
            tmp[j-1] = sum(p[:j])
        p = tmp

    print(p[-1])
