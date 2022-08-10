import sys
input = sys.stdin.readline

n = int(input())

dq = []

for _ in range(n):
    inp = list(input().split())
    cmd = inp[0]

    if cmd == 'push_front':
        dq.insert(0, inp[1])
    elif cmd == 'push_back':
        dq.append(inp[1])
    elif cmd == 'pop_front':
        if dq:
            print(dq.pop(0))
        else: print(-1)
    elif cmd == 'pop_back':
        if dq:
            print(dq.pop())
        else: print(-1)
    elif cmd == 'size':
        print(len(dq))
    elif cmd == 'empty':
        if not dq:
            print(1)
        else: print(0)
    elif cmd == 'front':
        if dq:
            print(dq[0])
        else: print(-1)
    else:
        if dq:
            print(dq[-1])
        else: print(-1)