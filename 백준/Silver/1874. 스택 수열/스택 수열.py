import sys
input = sys.stdin.readline

n = int(input())
stack = []
lst = [int(input()) for _ in range(n)]
# for i in range(1, n+1):
#     stack.insert(0, i)
#     print('+')
#     if i == lst[0]:
#         lst.pop(0)
#         print('-')
#         if not lst: break
#         while lst[0] < i:
#             lst.pop(0)
#             print('-')
#             if not lst: 
#                 break

i = 1
ans = ''
err = 0
while lst:
    if i <= n:
        stack.insert(0, i)
        ans += '+'
        if i == lst[0]:
            stack.pop(0)
            lst.pop(0)
            ans += '-'
        i+=1
    else:
        if stack != lst:
            err = 1
            break
    while stack and lst:
        if stack[0] == lst[0]:
            ans += '-'
            stack.pop(0)
            lst.pop(0)
        else: break

if err == 1: print('NO')
else:
    for i in ans: sys.stdout.write(str(i)+'\n')
