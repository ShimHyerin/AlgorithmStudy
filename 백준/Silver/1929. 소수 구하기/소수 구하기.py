import sys
input = sys.stdin.readline

n, m = map(int, input().split())

lst = [False, False] + [True]*(m-1) # 0, 1 -> False
prime = []

for i in range(2, m+1):
    if lst[i]: # i번째 idx가 배열에서 True일 때 (소수일 확률 O)
        prime.append(i)
        for j in range(2*i, m+1, i): # range(start, stop, step)
            # i의 배수는 소수가 아니므로 False로 처리
            lst[j] = False

for i in prime:
    if i >= n:
        print(i)