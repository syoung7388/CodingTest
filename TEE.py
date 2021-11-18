import sys
input = sys.stdin.readline


N, C, M = map(int, input().split())

arr =[tuple(map(int, input().split())) for _ in range(N)]

    
P = N*5
dp = [[[-1]*(P+1) for _ in range(C+1)] for _ in range(N+1)] 
dp[0][arr[0][0]][arr[0][1]] = arr[0][2]
res = 10000
for i in range(1, N+1):
    for j in range(C+1):
        for k in range(P+1):
            if dp[i][j][k] == -1: continue
            cpu, mem, prt = arr[i-1]
            dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-cpu][j-prt]+mem)
            
for p in range(P+1):
    if dp[N][C][p] >= M and res > p:
        res = p

if res == 10000:
    print(-1)
else:
    print(res)

