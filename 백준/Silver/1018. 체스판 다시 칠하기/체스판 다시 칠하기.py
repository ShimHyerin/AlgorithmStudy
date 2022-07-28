import sys
input = sys.stdin.readline

n, m = map(int, input().split())

chess = []
for _ in range(n):
    chess.append(input()[:-1]) # 빠른 입력으로 인한 줄바꿈 문자 슬라이싱

def sol(lst, cur):
    cnt = 0
    for i in range(8):
        if lst[i] != cur:
            cnt += 1
        if cur == 'W': cur = 'B'
        else: cur = 'W'
    return cnt

tmp1 = 0
tmp2 = 0
cnt = 100001
for k in range(m-7):
    for i in range(n-7):
        a = chess[n-8-i:n-i]
        for j in range(8):
            tmp = a[j]
            chessline = tmp[m-8-k:m-k]
            if j%2 == 0:
                tmp1 += sol(chessline, 'W')
                tmp2 += sol(chessline, 'B')
            else:
                tmp1 += sol(chessline, 'B')
                tmp2 += sol(chessline, 'W')
        cnt = min(tmp1, tmp2, cnt)
        tmp1 = 0
        tmp2 = 0

print(cnt)

