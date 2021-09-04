import math
def Move(l, r, flag):
    if dp[l][r][flag] != -1: return dp[l][r][flag]
    left = right =math.inf
    if flag == 0:
        cur = pos[l][0]
    else:
        cur = pos[r][0]
    
    on = light[N] - light[r] + light[l-1]
    
    if l > 1: #왼쪽으로 이동 가능
        left = Move(l-1, r, 0) + (cur - pos[l-1][0])*on
    if r < N:
        right = Move(l, r+1, 1)+(pos[r+1][0] - cur)*on
    
    dp[l][r][flag] = min(left, right)
    return dp[l][r][flag]
   
N, M = map(int, input().split())
pos = [(0, 0)]
for _ in range(N):
    pos.append(tuple(map(int, input().split())))

light = [0]*(N+1)
for l in range(1, N+1):
    light[l] =light[l-1]+pos[l][1]


dp = [[[-1]*2 for _ in range(N+1)] for _ in range(N+1)] 
dp[1][N][0]= dp[1][N][1] = 0

print(Move(M, M, 0))
