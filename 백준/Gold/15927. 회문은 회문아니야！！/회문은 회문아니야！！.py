import sys
input = sys.stdin.readline

s = input()[:-1]

if s == s[::-1]:
    if s.count(s[0]) == len(s): print(-1)
    else:
        cnt, tmp, chk = 2, 1, 0
        ans = 0
        while True:
            st = 0
            end = len(s) - tmp 
            for i in range(cnt):
                s_ = s[st:end]
                if s_ != s_[::-1]:
                    chk = 1
                    break
                st += 1
                end += 1
            if chk == 1: 
                break
            cnt += 1
            tmp += 1
        print(len(s_))


else: print(len(s))

