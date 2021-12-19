import sys
input = sys.stdin.readline
dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, -1, -1, -1, 0, 1, 1, 1]



def DFS(sx, sy, s, G, F):
    global res
    res = max(res, s)
    gra = [g[:] for g  in G]
    fish = [f[:] for f in F]

    for i in range(1, 17):
        if not fish[i]: continue
        x, y = fish[i]
        n, d = gra[x][y]
        if n == -1: continue
        for j in range(8):
            k = (d+j)%8

            xx, yy = dx[k]+x, dy[k]+y
            if not (0<=xx<N and 0<=yy<N) or gra[xx][yy][0] == -1: continue

            #물고기 변경
            gra[xx][yy], gra[x][y] = [gra[x][y][0], k], gra[xx][yy]
            fish[i] = [xx, yy]
            fish[gra[x][y][0]] = [x, y]

            break


  

    d = gra[sx][sy][1]
    gra[sx][sy] = [0, 0] #물고기 먹음
    for i in range(1, 5):
        xx, yy = i*dx[d]+sx, i*dy[d]+sy
        if not (0<=xx<N and 0<=yy<N) or gra[xx][yy][0] == 0: continue

        bf = gra[xx][yy][0]
        gra[xx][yy][0] = -1
        fish[bf] = []

        DFS(xx, yy, s+bf ,gra, fish)

        gra[xx][yy][0] = bf
        fish[bf] = [xx, yy]

        
        










N = 4
gra = []
fish = [[] for _ in range(17)]

for j in range(N):
    arr = list(map(int, input().split()))
    a = []
    for i in range(0, N*2, 2):
        n, d = arr[i], arr[i+1]
        a.append([n, d-1])
        fish[n] = [j, i//2]
    gra.append(a)

st = gra[0][0][0]
gra[0][0][0] = -1
fish[st] = []
res = 0
DFS(0, 0, st, gra, fish)


print(res)
