import sys
input = sys.stdin.readline

# input
n = int(input())
a = list(map(int, input().split()))

st = [] # stack
ans = [-1] * n # init

st.append(0)
for i in range(1, n):
    # 1) 스택이 비어있지 않음 2) 스택의 최상위에 있는 값이 현재 검사값(a[i])보다 작음
    while st and a[st[-1]] < a[i]:
        ans[st.pop()] = a[i] # 스택에서 pop하는 값의 오큰수는 현재 검사값임(a[i])
    st.append(i) # 스택에는 idx값을 저장함 -> 수열 배열에 쉽게 접근하기 위함

print(*ans)
