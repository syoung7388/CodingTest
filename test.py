from collections import deque
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def DFS(x, y):
    gra[x][y] = D
    for k in range(4):
        xx, yy = dx[k]+x, dy[k]+y
        if not (0<=xx<N and 0<=yy<N) or gra[xx][yy] < 0: continue
        if gra[xx][yy] == 1:
            DFS(xx, yy)
        else:
            if (x, y) not in Q:
                Q.append((x, y))
         

N = int(input())
gra = [list(map(int, input().split())) for _ in range(N)]

Q = deque()
D = -1
for i in range(N):
    for j in range(N):
        if gra[i][j] == 1:
            DFS(i, j)
            D -= 1
L = 0
res = 2147000000
while Q:
    L += 1
    for _ in range(len(Q)):
        x, y = Q.popleft()
        for k in range(4):
            xx, yy = dx[k]+x, dy[k]+y
            if not (0<=xx<N and 0<=yy<N): continue
            if gra[xx][yy] == 0:
                gra[xx][yy] = gra[x][y]
                Q.append((xx, yy))
            elif gra[x][y] < gra[xx][yy]:
                res = min(res, L*2-1)
            elif gra[x][y] > gra[xx][yy]:
                res = min(res, (L-1)*2)
print(res)
