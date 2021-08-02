from collections import deque
N, M = map(int,input().split())
gra = [list(map(int, input())) for _ in range(N)]
    
dis = [[0]*M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
Q = deque()
Q.append((0,0))
dis[0][0] =1

while Q:
    x, y = Q.popleft()
    gra[x][y] = 0
    if x == N and y == M:
        break
    for k in range(4):
        xx = dx[k]+x
        yy = dy[k]+y
        if 0<=xx<N and 0<=yy<M and gra[xx][yy] == 1:
            dis[xx][yy] =dis[x][y]+1
            Q.append((xx, yy))
print(dis[N-1][M-1])
