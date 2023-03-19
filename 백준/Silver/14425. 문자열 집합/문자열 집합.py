m, s = map(int, input().split())
li = []
cnt = 0
for i in range(m):
    li.append(input())
for i in range(s):
    a = input()
    if a in li: cnt += 1
print(cnt)
