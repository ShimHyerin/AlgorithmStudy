import sys
input = sys.stdin.readline

li = []
idx = []
min_ = 151 # init
for i in range(1, 9):
    sc = int(input()) # input score
    if i < 6:
        li.append(sc)
        idx.append(i)
        if sc < min_: min_ = sc
    else:
        if sc > min_:
            li.append(sc)
            idx.append(i)
            idx.pop(li.index(min_))
            li.pop(li.index(min_))
            min_ = min(li)

print(sum(li))
print(*idx)