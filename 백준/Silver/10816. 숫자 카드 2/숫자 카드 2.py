n = int(input())
l = list(map(int, input().split()))
m = int(input())
card = list(map(int, input().split()))

anw = ''
d = dict()
for i in l:
    if i in d: d[i] += 1
    else: d[i] = 1
for i in card:
    if i in d: anw += str(d[i]) + ' '
    else: anw += '0 '
print(anw)