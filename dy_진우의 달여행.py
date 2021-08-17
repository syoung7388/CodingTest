import sys
N, M = map(int, input().split())
Max = sys.maxsize
gra= [list(map(int, input().split())) for _ in range(N)]
dis = [[[Max]*3 for _ in range(M)] for _ in range(N)]
dis[0] =[[x, x, x] for x in gra[0]]

for i in range(1, N):
    for j in range(M):
        dis[i][j][0] = min(dis[i-1][j-1][1], dis[i-1][j-1][2])+gra[i][j] if j != 0 else Max

        dis[i][j][1] = min(dis[i-1][j][0], dis[i-1][j][2])+gra[i][j]

        dis[i][j][2]  = min(dis[i-1][j+1][0], dis[i-1][j+1][1])+gra[i][j] if j != M-1 else Max


        
res = Max


for r in dis[-1]:
    res = min(res, min(r))

print(res)
