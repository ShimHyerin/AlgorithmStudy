import sys
input = sys.stdin.readline

from collections import Counter

n = int(input())
li = []
for _ in range(n):
  li.append(input().rstrip())

li.sort()
most = Counter(li).most_common(1)
print(most[0][0])