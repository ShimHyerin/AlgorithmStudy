import sys
input = sys.stdin.readline

# input

e_, s_, m_ = map(int, input().split())

e, s, m = 0, 0, 0
cnt = 0

while True:
  if e == 15: e = 0
  if s == 28: s = 0
  if m == 19: m = 0

  e, s, m = e+1, s+1, m+1
  cnt += 1

  if e_ == e and s_ == s and m_ == m: break

print(cnt)