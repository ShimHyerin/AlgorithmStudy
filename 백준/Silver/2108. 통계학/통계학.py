import sys
from collections import Counter

input = sys.stdin.readline

# 최빈값 구하는 함수
def mc(xs):
    if n == 1: return lst[0]
    c = Counter(xs).most_common(2)
    return (c[1][0] if c[0][1] == c[1][1] else c[0][0])

n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

lst.sort()
# 산술 평균
sum = 0
for i in lst:
    sum += i
print(int(round(sum/n, 0)))
print(lst[n//2]) # 중앙값
print(mc(lst)) # 최빈값
print(lst[-1] - lst[0]) # 범위