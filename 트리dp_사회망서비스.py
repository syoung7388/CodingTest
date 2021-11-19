import sys
input = sys.stdin.readline
def Inside(node):
    ch[node] = 1
    for g in G[node]:
        if ch[g] == 1: continue
        Inside(g)
        dp[node][0] += dp[g][1]
        dp[node][1] += min(dp[g][0], dp[g][1])


 
    
N = int(input())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
    
dp = [[0, 1] for _ in range(N+1)]
ch = [0]*(N+1)
Inside(1)

print(min(dp[1][0], dp[1][1]))
