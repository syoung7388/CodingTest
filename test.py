from collections import deque
import math
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
def BFS(x, y):
    Q = deque([(x, y)])
    dis[x][y] = 0
    while Q:
        x, y = Q.popleft()
        for k in range(4):
            xx, yy = dx[k]+x, dy[k]+y
            while True:
                if not (0<=xx<H and 0<=yy<W): break
                if gra[xx][yy] == '*': break
                if dis[x][y]+1 > dis[xx][yy]: break

                Q.append((xx, yy))
                dis[xx][yy] = dis[x][y]+1
                xx, yy = xx+dx[k], yy+dy[k]
    


W, H = map(int, input().split())

gra = [list(map(str, input())) for _ in range(H)]

C = []
for i in range(H):
    for j in range(W):
        if gra[i][j] == 'C':
            C.append((i, j))

(sx, sy), (ex, ey) = C
Max = math.inf
dis = [[Max]*W for _ in range(H)]
BFS(sx, sy)

print(dis[ex][ey] -1)
