import sys
input = sys.stdin.readline

while True:
  s = input().rstrip()
  if s == 'end': break

  flag = 1
  vowel = ['a', 'e', 'i', 'o', 'u']

  if 'a' not in s and 'e' not in s and 'i' not in s and 'o' not in s and 'u' not in s:
    flag = 0
    print(f'<{s}> is not acceptable.')
    continue
  
  else:
    co, vo, bef = 0, 0, ''
    for i in s:
      if i in vowel:
        if (i == 'e' and bef == 'e') or (i == 'o' and bef == 'o'):
          pass
        elif i == bef:
          flag = 0
          break
        vo += 1
        co = 0

        if vo == 3:
          flag = 0
          break

      else: # 자음
        if i == bef:
          flag = 0
          break
        co += 1
        vo = 0
        if co == 3:
          flag = 0
          break

      bef = i

  if flag == 0:
    print(f'<{s}> is not acceptable.')
  else:
    print(f'<{s}> is acceptable.')