import sys
input = sys.stdin.readline

# input
a = len(input().strip())
b = len(input().strip())

if a >= b:
    print('go')
else:
    print('no')

