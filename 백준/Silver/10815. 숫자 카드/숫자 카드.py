n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
inter = set(a) & set(b)
s = ''
for i in b:
    if i in inter:
        s += '1 '
    else: s += '0 '
print(s)