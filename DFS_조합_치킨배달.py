def DFS(L, k):
    global res
    if L == M:
        tot_dis = 0
        for hx, hy in home:
            min_dis = 2147000000
            for i in range(M):
                cx, cy = chicken[P[i]]
                min_dis = min(abs(hx-cx)+abs(hy-cy), min_dis)
            tot_dis += min_dis
        res = min(res, tot_dis)
        return
    if k >= C: return

    P[L] = k
    DFS(L+1, k+1)
    DFS(L, k+1)



N, M = map(int, input().split())
gra = [list(map(int, input().split())) for _ in range(N)]

home = []
chicken = []
for i in range(N):
    for j in range(N):
        if gra[i][j] == 1:
            home.append((i, j))
        elif gra[i][j] == 2:
            chicken.append((i, j))
C = len(chicken)

P = [0]*(M)
res = 2147000000
DFS(0, 0) #M = 고른 개수 k = 치킨집 번호

print(res)

