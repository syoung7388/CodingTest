from collections import deque
N, M = map(int, input().split())
water = deque()
Q = deque()
gra = [list(map(str, input())) for _ in range(N)]
dis = [[-1]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if gra[i][j] == '*':
            water.append((i, j))
        if gra[i][j] == 'S':
            dis[i][j] = 0
            Q.append((i, j))
        if gra[i][j] == 'D':
            end = (i, j)

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
     

while Q:
    for _ in range(len(water)):
        wx, wy = water.popleft()
        for k in range(4):
            wxx, wyy = dx[k]+wx, dy[k]+wy
            if 0<=wxx<N and 0<=wyy<M and gra[wxx][wyy] == '.' and dis[wxx][wyy] == -1:
                water.append((wxx, wyy))
                gra[wxx][wyy] = '*'

    x, y = Q.popleft()
    for h in range(4):
        xx, yy = dx[h]+x, dy[h]+y
        if not (0<=xx<N and 0<=yy<M) or gra[xx][yy] == '*':
            continue
        if  (gra[xx][yy] == '.' or gra[xx][yy] == 'D') and dis[xx][yy] == -1:
            dis[xx][yy]= dis[x][y]+1
            Q.append((xx, yy))
if dis[end[0]][end[1]] == -1:
    print("KAKTUS")
else:
    print(dis[end[0]][end[1]])
