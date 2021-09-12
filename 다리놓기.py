for _ in range(int(input())):
    N, M = map(int, input().split())
    
    dp= [[0]*(M+1) for _ in range(N+1)]
    
    for l in range(1, M-N+1+1):
        dp[1][l] = dp[1][l-1]+1

    for i in range(2, N+1):
        for j in range(i, M-N+i+1):
            dp[i][j] = dp[i-1][j-1]+dp[i][j-1]

    print(dp[-1][-1])
