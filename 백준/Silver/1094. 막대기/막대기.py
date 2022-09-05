import sys
input = sys.stdin.readline

from collections import Counter

# input
x = bin(int(input()))

print(Counter(x)['1'])
