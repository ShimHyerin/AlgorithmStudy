import sys
input = sys.stdin.readline

def sol(li, mode, cnt):
    for i in range(8):
        if mode=='even':
            if i%2==0 and li[i] == 'F': cnt += 1
        else:
            if i%2==1 and li[i] == 'F': cnt += 1
    return cnt

cnt = 0
for i in range(8):
    li = input()
    if i%2 == 0:
        cnt = sol(li, 'even', cnt)
    else:
        cnt = sol(li, 'odd', cnt)
print(cnt)