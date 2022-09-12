import sys
input = sys.stdin.readline

s = input().rstrip()
st = []
cnt = 0
for i in s:
    if i == '(':
        st.append(i)
    else:
        if st: st.pop()
        else: cnt += 1
cnt += len(st)
print(cnt)