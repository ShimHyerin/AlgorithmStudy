n = int(input())
for i in range(n):
    s =input().split('()')
    ss = ''
    for i in s:
        ss+= i
    while len(s)//2:
        s = ss.split('()')
        ss = ''
        for i in s:
            ss+= i
    if len(ss) == 0: print('YES')
    else: print('NO')