N = int(input())
gra = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(N) for _ in range(N)]
dp[0] = gra[0]
for i in range(1, N):
    for j in range(N):
        mins = 2147000000
        for k in range(N):
            if k == j: continue
            mins = min(dp[i-1][k], mins)
        dp[i][j] = mins + gra[i][j]        

for d in dp:
    print(d)
print()

for g in gra:
    print(g)
print()

print(min(dp[-1]))
