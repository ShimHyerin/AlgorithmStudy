l = []
n = int(input())
for i in range(n):
    tmp = int(input())
    if tmp == 0: l.pop(-1)
    else: l.append(tmp)
print(sum(l))