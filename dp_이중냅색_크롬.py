import sys
input = sys.stdin.readline
#이문제의point)
"""
어멋 priority 범위 0<= priority <= 5 ? 작네?
그럼 1~i번 창을 고려했을때 Cpu값이 j 이면서 priority 범위가 k인 메모리의 max값은 ? 
"""


N, C, M = map(int, input().split())

cpu = [0]*N
mem = [0]*N
pri = [0]*N

for i in range(N):
    c,m,p = map(int, input().split())
    cpu[i], mem[i], pri[i] = c, m, p
    
P = N*5
dp = [[[-1]*(P+1) for _ in range(C+1)] for _ in range(N+1)] 
dp[0][0][0] = 0 

res = 10000

for i in range(N):
    for j in range(C+1): 
        for k in range(P+1): 

            if dp[i][j][k] == -1: continue
            print(i, j, k)
            ncpu = min(j+cpu[i], C)
            
            dp[i+1][j][k] = max(dp[i][j][k], dp[i+1][j][k])

            dp[i+1][ncpu][k+pri[i]] = max(dp[i][j][k]+mem[i],
                                           dp[i+1][ncpu][k+pri[i]]
                                          )

        
for p in range(P+1):
    if dp[N][C][p] >= M and res > p:
        res = p

if res == 10000:
    print(-1)
else:
    print(res)
