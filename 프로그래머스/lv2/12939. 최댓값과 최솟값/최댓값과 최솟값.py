def solution(s):
    li = list(map(int, s.split()))
    s = f"{min(li)} {max(li)}"
    return s