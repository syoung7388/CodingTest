N, C, M = map(int, input().split())
P = N*5

tab = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[[-1]*(P+1) for _ in range(C+1)] for _ in range(N+1)]
dp[0][0][0] = 0

for i in range(N):
    for j in range(C+1):
        for k in range(P+1):
            if dp[i][j][k] == -1: continue
            dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j][k])
            cpu, mem, prt = tab[i]
            cpu = min(j+cpu, C)
            dp[i+1][cpu][k+prt] = max(dp[i+1][cpu][k+prt], dp[i][j][k]+mem)
res = 2147000000
for i in range(1, P+1):
    if dp[N][C][i] >= M and i < res:
        res = i
if res == 2147000000:
    print(-1)
else:
    print(res)    
