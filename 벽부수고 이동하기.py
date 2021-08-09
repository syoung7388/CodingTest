from collections import deque
import sys

N, M = map(int, input().split())
gra = [list(map(int, input())) for _ in range(N)]
dis = [[[-1]*2 for _ in range(M)] for _ in range(N)]
# 0 => 벽 안부슴, 1 => 벽 부슴
dis[0][0][0] = 1
Q = deque([(0,0,0)])
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1 ]
while Q:
    x, y, cnt = Q.popleft()
    if (x , y) == (N-1, M-1):
        break
    for k in range(4):
        xx, yy = dx[k]+x, dy[k]+y
        if 0<=xx<N and 0<=yy<M:
            if gra[xx][yy] == 0 and dis[xx][yy][cnt] == -1:
                dis[xx][yy][cnt] = dis[x][y][cnt] +1
                Q.append((xx, yy, cnt))
            elif cnt == 0 and gra[xx][yy] == 1 and dis[xx][yy][1] == -1:
                dis[xx][yy][1] = dis[x][y][cnt]+1
                Q.append((xx, yy,1))
                
a1 , a2 = dis[N-1][M-1][0], dis[N-1][M-1][1]

if a1 == -1 and a2 != -1:
    print(a2)
elif a1 != -1 and a2 == -1:
    print(a1)
else:
    print(min(a1, a2))
