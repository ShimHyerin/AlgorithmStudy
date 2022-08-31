import sys
input = sys.stdin.readline

n = int(input())

li = [n-i+1 for i in range(1, n+1)]
ans = []

while len(li)>1:
  ans.append(li.pop())
  li.insert(0, li.pop())
ans.append(li[0])
print(*ans)