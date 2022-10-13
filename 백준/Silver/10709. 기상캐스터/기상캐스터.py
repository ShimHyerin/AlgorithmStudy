import sys
input = sys.stdin.readline

n, m = map(int, input().split())
for i in range(n):
    li = input().rstrip()
    cur = ''
    cnt = 0 
    for j in li:
        if cnt > 0 and j == '.':
            print(cnt,end=' ')
            cnt += 1
        elif cnt > 0 and j == 'c':
            cnt = 0
            print(cnt,end=' ')
            cnt += 1
        elif cnt == 0 and j == 'c':
            print(cnt,end=' ')
            cnt += 1
        else: print('-1',end=' ')
    print()