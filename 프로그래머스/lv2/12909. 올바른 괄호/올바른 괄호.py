def solution(s):
    st = []
    tg = 0
    for i in s:
        if i == '(':
            st.append(i)
        else: # i == ')'
            if st: st.pop()
            else: return False
    if st: return False
    return True