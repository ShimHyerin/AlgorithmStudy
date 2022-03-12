n = int(input())
l = []
for i in range(n):
    a = input().split()
    a = [int(x) for x in a]
    l.append(a)

for i in range(1, len(l)):
    l[i][0] = min(l[i-1][1], l[i-1][2]) + l[i][0]
    l[i][1] = min(l[i - 1][0], l[i - 1][2]) + l[i][1]
    l[i][2] = min(l[i - 1][0], l[i - 1][1]) + l[i][2]

print(min(l[n-1][0], l[n-1][1], l[n-1][2]))