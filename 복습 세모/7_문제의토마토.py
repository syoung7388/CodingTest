

from collections import deque


M, N = map(int ,input().split())
box = [list(map(int, input().split())) for _ in range(N)]
ch = [[0]*M for _ in range(N)]
Q = deque()
dx = [-1,0,1,0]
dy=[0,1,0,-1]

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            Q.append((i, j))


bf = -3
while Q:
    x, y = Q.popleft()
    for l in range(4):
        xx = x+dx[l]
        yy = y+dy[l]
        if 0<=xx<N and 0<=yy<M and box[xx][yy]==0:
            box[xx][yy] = 1
            ch[xx][yy] = ch[x][y]+1
            Q.append((xx,yy))
            bf = max(ch[xx][yy], bf)


flag =0
for a in range(N):
    for b in range(M):
        if box[a][b] == 0:
            flag =1
            break

if flag == 1:
    print(-1)
else:
    print(bf)


    


