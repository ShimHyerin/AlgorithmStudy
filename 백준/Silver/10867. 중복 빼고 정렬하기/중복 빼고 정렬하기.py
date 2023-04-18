import sys
input = sys.stdin.readline

n = int(input())
li = list(set(map(int, input().split())))

print(*sorted(li), sep=' ')