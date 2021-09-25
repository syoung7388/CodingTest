N = int(input())

dp = [[0]*3 for _ in range(N)]
dp[0] = [1, 1, 1]

for i in range(1, N):
    dp[i][0] = dp[i-1][1]+dp[i-1][2]
    dp[i][1] = dp[i-1][0]+dp[i-1][2]
    dp[i][2] = dp[i-1][0]+dp[i-1][1]+dp[i-1][2]
print(sum(dp[-1])%9901)
    
