import sys
def Trade(l, bit, m):
    if dp[bit][l] != 0: return dp[bit][l]
    
    for i in range(N):
        if gra[l][i] < m or bit & (1<<i) != 0: continue
        dp[bit][l] = max(Trade(i, bit|(1<<i), gra[l][i])+1, dp[bit][l])
       
    return dp[bit][l]
        
        
            
    
N = int(input())
gra = [list(map(int, input())) for _ in range(N)]
dp = [[0]*(N) for _ in range(1<<N+1)]

print(Trade(0, 1<<0, 0)+1)
