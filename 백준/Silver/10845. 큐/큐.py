import sys
input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    a = input().split()
    if a[0] == "push":
        q.insert(0, int(a[1]))
    elif a[0] == "front":
        if q: print(q[-1])
        else: print(-1)
    elif a[0] == "back":
        if q: print(q[0])
        else: print(-1)
    elif a[0] == "pop":
        if q: 
            print(q[-1])
            q.pop()
        else: print(-1)
    elif a[0] == "size":
        print(len(q))
    else:
        if q: print(0)
        else: print(1)