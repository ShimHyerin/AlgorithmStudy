n = int(input())

def sol(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return sol(n-1) + sol(n-2)
print(sol(n))