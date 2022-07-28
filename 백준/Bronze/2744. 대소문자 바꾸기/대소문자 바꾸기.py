import sys
input = sys.stdin.readline

s = input()
ans = ''
for i in s:
    if i.isupper() is True: ans += i.lower()
    else: ans += i. upper()
print(ans)