import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

#main
N = int(input())
um = [0]+list(map(int, input().split()))
dp = [[-1]*(N+1) for _ in range(N+1)]

def getHim(now, next):
    return abs(um[now]-um[next])

def Choose(x, y):
    if x == N or y == N: return 0
    if dp[x][y] != -1: return dp[x][y]
    
    pick= max(x, y)+1

    if x == 0:
        dp[x][y] = min(Choose(pick, y),Choose(x, pick)+getHim(y, pick))
    elif y == 0:
        dp[x][y] = min(Choose(pick, y)+getHim(x, pick), Choose(x, pick))
    else:
        dp[x][y] = min(Choose(pick, y)+getHim(x, pick), 
                   Choose(x, pick)+getHim(y, pick))
    return dp[x][y]
    
#res
print(Choose(0,0))


