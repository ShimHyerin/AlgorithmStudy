import sys
input = sys.stdin.readline

t = int(input())  
for _ in range(t):
    n = int(input())
    dic = {}
    cnt = 1
    for i in range(n):
        tmp = input().split()
        if tmp[1] not in dic:
            dic[tmp[1]] = []
        dic[tmp[1]].append(tmp[0])
    for i in dic:
        cnt *= (len(dic[i])+1)
    print(cnt - 1)
    
