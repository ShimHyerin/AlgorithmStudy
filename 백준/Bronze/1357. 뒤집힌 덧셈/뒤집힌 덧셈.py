import sys
input = sys.stdin.readline

def Rev(x):
    return int(x[::-1])
li = input().split()
print(Rev(str(Rev(li[0])+Rev(li[1]))))