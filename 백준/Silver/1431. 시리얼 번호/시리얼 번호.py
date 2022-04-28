import sys
input = sys.stdin.readline

n = int(input())
snumber = [] # serial number list

# input
for _ in range(n):
    snumber.append(input().strip())

def snumber_sum(snum):
    res = 0
    for i in snum:
        if i.isdigit(): res += int(i)
    return res

snumber.sort(key=lambda x: (len(x), snumber_sum(x), x))

# output
for i in snumber:
    print(i)