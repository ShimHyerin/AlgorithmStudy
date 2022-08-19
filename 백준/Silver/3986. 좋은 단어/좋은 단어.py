import sys
input = sys.stdin.readline

# input
n = int(input())


cnt = 0 # Variable to count 'good words'
for _ in range(n):
    word = input()[:-1]
    st = [] # stack init
    for cur in word: # current letter
        if st:
            lat = st[-1] # latest letter
            st.append(cur)
            if lat == cur:
                st.pop()
                st.pop()
        else:
            st.append(cur)

    # It's a good word if the stack is empty
    if not st:
        cnt += 1
print(cnt)