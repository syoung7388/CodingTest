def U(now):
    ch[now] = 1
    
    for nt in G[now]:
        if ch[nt] == 1: continue
        U(nt)
        dp[now][0] += max(dp[nt][0], dp[nt][1])
        dp[now][1] += dp[nt][0]
    
        
    return     
        


n = int(input())
cost= [0] + list(map(int, input().split()))

dp = [[0,cost[x]] for x in range(n+1)] 
G= [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

ch = [0]*(n+1)
U(1)
print(max(dp[1][0], dp[1][1]))
