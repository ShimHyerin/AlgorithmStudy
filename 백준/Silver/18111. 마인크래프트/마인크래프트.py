import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
B_ = B # init
ground = []
for _ in range(N):
    tmp = list(map(int, input().split(' ')))
    for i in tmp: ground.append(i)
    # ground.append(tmp)

ground.sort(reverse=True)
check = [0]*257
ans, high = int(2e20), 0

for i in range(257):
    time = 0
    B = B_
    for j in ground:
        cur = j # current block
        if cur < i:
            if B < i-cur: 
                time = -1
                break
            time += i-cur
            B -= i-cur
        elif cur > i:
            time += (cur-i)*2
            B += cur-i
    check[i] = time
    if -1 < time <= ans:
        ans = time
        high = i
    # print(time, i)

print(ans, high)
