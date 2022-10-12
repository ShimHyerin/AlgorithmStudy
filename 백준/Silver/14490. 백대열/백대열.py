import sys
input = sys.stdin.readline

import math
n, m = map(int, input().split(':'))

tmp = math.gcd(n, m)
print(f'{n//tmp}:{m//tmp}')