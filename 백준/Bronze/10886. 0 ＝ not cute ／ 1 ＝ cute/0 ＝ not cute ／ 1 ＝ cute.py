n = int(input())
li = [0, 0]
for i in range(n):
    if int(input()) == 0:
        li[0] += 1
    else: li[1] += 1

if li[0] > li[1]: print('Junhee is not cute!')
else: print('Junhee is cute!')