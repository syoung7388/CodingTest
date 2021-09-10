import sys
sys.setrecursionlimit(10**6)
def getHims(now, next):
    if now == 0:
        return 0
    return abs(um[next-1]-um[now-1])

def Pick(x, y):
    
    if x > N-1 or y > N-1: return 0
    if dp[x][y] != -1:
        return dp[x][y]
    next = max(x, y)+1
    duck = Pick(next, y) + getHims(x, next)
    won = Pick(x, next)+getHims(y, next)
    
    dp[x][y] = min(duck, won)
    return dp[x][y]


N = int(input())
um = list(map(int, input().split()))
dp = [[-1]*(N+1) for _ in range(N+1)]
print(Pick(0, 0))
