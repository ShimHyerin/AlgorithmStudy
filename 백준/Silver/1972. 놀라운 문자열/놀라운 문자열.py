import sys
input = sys.stdin.readline

def sol(s):
  D = []
  for i in range(1, len(s)):
    for j in range(len(s)-i):
      tmp = s[j]+s[i+j]
      if tmp not in D:
        D.append(tmp)
      else: return "is NOT surprising."
    D = []
  
  return "is surprising."

while True:
  s = input().rstrip()
  if s == '*': break

  print(s, sol(s))