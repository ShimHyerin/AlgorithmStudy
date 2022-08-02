import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    if n == 1:
        tmp = int(input())
        print(1)
    else:
        que = list(map(int, input().split()))
        docs = [i for i in range(n)]
        cnt = 0
        while True:
            max_ = max(que)
            if max_ == que[0]:
                cnt += 1
                if docs[0] == m:
                    print(cnt)
                    break
                que.pop(0)
                docs.pop(0)

            else:
                que.append(que[0])
                que.pop(0)
                docs.append(docs[0])
                docs.pop(0)
                