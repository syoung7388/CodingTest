import sys
input = sys.stdin.readline
def SNS(now):
    ch[now] = 1
    for g in G[now]:
        if ch[g] == 1: continue
        SNS(g)
        dp[now][0] += min(dp[g][1], dp[g][0])
        dp[now][1] += dp[g][0]
    return
    
    
    
N = int(input())

G = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
ch = [0]*(N+1)
dp = [[1, 0] for _ in range(N+1)]
SNS(1)

print(min(dp[1][0], dp[1][1]))

