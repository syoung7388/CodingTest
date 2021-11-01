from collections import deque

N= 5
gra = [list(map(str, input())) for _ in range(N)]
Q = deque()
cnt = 0
for i in range(N):
    for j in range(N):
        if gra[i][j] == '*':
            Q.append((i, j, cnt))
            cnt += 1

dis = [[[-1]*(cnt) for _ in range(N)] for _ in range(N)]


for qx, qy, qc in Q:
    dis[qx][qy][qc] = 0
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


st = ()

while Q:
    x, y, n = Q.popleft()
    
    bit = (1<<n)
    s = 0
    for k in range(4):
        xx, yy = dx[k]+x, dy[k]+y
        if not (0<=xx<N and 0<=yy<N): continue
        if dis[xx][yy][n] == -1:
            dis[xx][yy][n] = dis[x][y][n] + 1
            Q.append((xx, yy, n))
        for i in range(cnt):
            if i == n: continue
            if dis[xx][yy][i] != -1:
                bit |= 1<<i
    if bit == ((1<<cnt)-1):
        st = (x, y, n)
        break




    
