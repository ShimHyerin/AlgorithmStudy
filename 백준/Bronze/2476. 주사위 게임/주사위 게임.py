import sys
input = sys.stdin.readline

n = int(input())

dice = [0]*6
ans = 0
for _ in range(n):
    li = list(map(int, input().split()))
    for i in li:
        dice[i-1] += 1
    if 3 in dice: 
        tmp = 10000+ (dice.index(3)+1)*1000
    elif 2 in dice:
        tmp = 1000 + (dice.index(2)+1)*100
    else:
        tmp = max(li)*100
    dice = [0]*6
    ans = max(ans, tmp)
print(ans)
