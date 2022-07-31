import sys
input = sys.stdin.readline

n = int(input())

lst = [False, False] + [True]*(1004000-1) # 0, 1 -> False
cnt = 0
i = 2
while True:
    if lst[i]:
        if i >= n and str(i) == str(i)[::-1]:
            print(i)
            break
        for j in range(2*i, 1004001, i): # range(start, stop, step)
            lst[j] = False
    i += 1
    
    