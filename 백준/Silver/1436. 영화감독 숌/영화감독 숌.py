import sys
input = sys.stdin.readline

n = int(input())
m = 666

while n != 0:
    if '666' in str(m): n -= 1
    if n == 0: break
    m += 1
print(m)