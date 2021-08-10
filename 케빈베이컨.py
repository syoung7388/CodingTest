N, M = map(int, input().split())
Max = N*N + 5
dis = [[Max]*N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    dis[a-1][b-1] = 1
    dis[b-1][a-1] = 1
for l in range(N):
    dis[l][l] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            dis[i][j] = min(dis[i][k]+dis[k][j], dis[i][j])
res = list()
for n in range(N):
    res.append(sum(dis[n]))

print(res.index(min(res))+1)

