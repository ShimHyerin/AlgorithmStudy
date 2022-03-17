n, m = map(int, input().split())
d = dict()
for _ in range(n):
    a = input().split(' ')
    d[a[0]] = a[1]

for _ in range(m):
    # site = input()
    print(d[input()])