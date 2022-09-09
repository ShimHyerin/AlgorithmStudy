import sys
input = sys.stdin.readline

from collections import Counter

s = input().rstrip()
ans = ['-']*len(s)
counter = Counter(s)
counter_li = list(counter)
li = []
flag = 1

for i in counter_li:
    cnt = counter[i]
    if cnt % 2 != 0:
        if len(s) % 2 == 0:
            print("I'm Sorry Hansoo")
            flag = 0
            break
        else:
            if ans[len(s)//2] == '-': 
                ans[len(s)//2] = i
                if cnt > 1:
                    for _ in range((cnt-1)//2):
                        li.append(i)
            else:
                print("I'm Sorry Hansoo")
                flag = 0
                break
    else:
        for _ in range(cnt//2):
            li.append(i)


if flag == 1:
    li = sorted(li)
    for i in range(len(li)):
        ans[i], ans[-1-i] = li[i], li[i]

    print(*ans, sep='')