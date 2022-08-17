n = int(input())
l = []
for i in range(n):
    s = input()
    l.append(s)
l = set(l)
x = sorted(list(l))
x = sorted(list(x), key=lambda x: len(x))
for i in x:
    print(i)