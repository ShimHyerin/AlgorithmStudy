import sys
input = sys.stdin.readline

from collections import Counter

# input
n = int(input())
msg = input().rstrip()

table = [0]*n 
tmp = 0

for i in range(1, n):
  while tmp > 0 and msg[i] != msg[tmp]:
    tmp = table[tmp-1]
  if msg[i] == msg[tmp]:
    tmp += 1
    table[i] = tmp
print(n-table[n-1])