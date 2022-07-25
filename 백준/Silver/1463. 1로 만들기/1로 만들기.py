n = int(input())

dp = [0] * (n+1) # init

# DP - Tabulation (상향식)
# (조건1) x % 3 == 0: x // 3, (조건2) x % 2 == 0: x // 2, (조건3) x - 1
for i in range(2, n+1): # 하위값부터 연산 횟수 저장
    # dp[i]에 i가 1이 되는 연산 횟수를 저장
    dp[i] = dp[i-1] + 1 # dp[i-1]: 1을 뺀 경우(조건3), +1: 연산 횟수 count
    if i % 3 == 0: # 조건1
        dp[i] = min(dp[i], dp[i//3] + 1) # 1을 뺐을 때와 3으로 나누었을 때의 횟수 중 최솟값 저장
    if i % 2 == 0: # 조건1
        dp[i] = min(dp[i], dp[i//2] + 1) # 1을 뺐을 때와 2으로 나누었을 때의 횟수 중 최솟값 저장

print(dp[n])