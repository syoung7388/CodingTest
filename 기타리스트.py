


N, S, M = map(int, input().split())

volume = list(map(int, input().split()))

dp = [[0]*(M+1) for _ in range(N+1)]

dp[0][S] = 1

for i in range(N):
    for j in range(M+1):
        if dp[i][j] == 1:
            nt = j +volume[i]
            if nt <= M:
                dp[i+1][nt] = 1
            
            nt = j - volume[i]
            if 0<= nt:
                dp[i+1][nt] = 1

for i in range(M, -1, -1):
    if dp[-1][i] == 1:
        print(i)
        break
else:
    print(-1)
