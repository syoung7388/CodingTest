import sys
input = sys.stdin.readline

N, C, M = map(int, input().split())
tab = [list(map(int, input().split())) for _ in range(N)]

P = 5*101
dp = [[[-1]*(P+1) for _ in range(C+1)] for _ in range(N+1)]
dp[0][0][0] = 0
for i in range(N):
    for j in range(C+1):
        for p in range(P+1):
            if dp[i][j][p] == -1: continue
            c, m, pr = tab[i]
            dp[i+1][j][p] = max(dp[i][j][p], dp[i+1][j][p])
            c = min(C, c+j)
            dp[i+1][c][p+pr] = max(dp[i+1][c][p+pr], dp[i][j][p]+m)
res = -1
for i in range(1, P):
    if dp[-1][C][i] >= M:
        res = i
        break
print(res)
