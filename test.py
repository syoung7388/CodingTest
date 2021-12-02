import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def Z(lt, rt, f):
    if dp[lt][rt][f] != -1: return dp[lt][rt][f]
    
    if f:
        cur = rt
    else:
        cur = lt
        
    on = watt[-1] -watt[rt] + watt[lt-1]
    
    left = right = 2147000000
    if lt > 1 :
        left = Z(lt-1, rt, 0) + (dis[cur] - dis[lt-1])*on
    if rt < N:
        right = Z(lt, rt+1, 1) + (dis[rt+1]-dis[cur])*on
    dp[lt][rt][f] = min(left, right)
    return dp[lt][rt][f]

        
    
N, M = map(int, input().split())

dis = [0]
watt = [0]
for _ in range(N):
    a, b = map(int, input().split())
    dis.append(a)
    watt.append(watt[-1]+b)

dp = [[[-1]*2 for _ in range(N+1)] for _ in range(N+1)]
dp[1][N][0] = dp[1][N][1] = 0
print(Z(M, M, 0))
