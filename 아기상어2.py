from collections import deque


if __name__ == "__main__":
    N, M = map(int, input().split())  
    gra = [list(map(int, input().split())) for _ in range(N)]
    dx = [-1, -1, -1, 0,  0,  1,  1,  1]
    dy = [-1, 0, 1, -1,  1,-1, 0, 1]

    Q= deque()
    for i in range(N):
        for j in range(M):
            if gra[i][j] == 1:
                Q.append((i, j))

    res = 0
    while Q:
        x, y = Q.popleft()
        for k in range(8):
            xx = x+dx[k]
            yy = y+dy[k]
            if 0<=xx<N and 0<=yy<M and gra[xx][yy]==0:
                gra[xx][yy] = gra[x][y]+1
                res = max(res,gra[xx][yy])
                Q.append((xx, yy))
    print(res-1)
    for g in gra:
        print(g)
