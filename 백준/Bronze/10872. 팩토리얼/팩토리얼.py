import sys
input = sys.stdin.readline

n = int(input())
def sol(n):
    tmp = 1
    for i in range(1, n+1):
        tmp *= i
    return tmp

print(sol(n))