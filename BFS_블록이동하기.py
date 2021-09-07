from collections import deque


def solution(gra):
    N = len(gra)
    dis = [[[-1]*2 for _ in range(N)] for _ in range(N)]
    Q = deque()
    Q.append((0, 1, 0))
    dis[0][1][0] = 0
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    while Q:
        x, y, d = Q.popleft()
        if x == N-1 and y == N-1:
            return dis[x][y][d]
    
        # 방향 그대로
        for k in range(4):
            xx, yy = x+dx[k], y+dy[k]
            if xx >= N or yy >=N or gra[xx][yy] == 1: continue
            if dis[xx][yy][d] == -1:
                Q.append((xx, yy, d))
                dis[xx][yy][d] = dis[x][y][d] + 1
        
        #방향전환  가로:0   세로:1
        
        if d == 0: #가로 -> 세로
            if 0<=x-1 and 0 <= y-1 and gra[x-1][y-1] == 0 and gra[x-1][y] ==0 and dis[x-1][y-1][1] == -1:
                dis[x-1][y-1][1] = dis[x][y][d] + 1
                Q.append((x-1, y-1, 1))
            if x+1 < N and 0 <= y-1 and gra[x+1][y-1] == 0 and gra[x+1][y]==0 and dis[x+1][y-1][1] == -1:
                dis[x+1][y-1][1] = dis[x][y][d] + 1
                Q.append((x+1, y-1, 1))
                
        elif d == 1: #세로 -> 가로
            if 0 <= x-1 and 0 <= y-1 and gra[x-1][y-1] == 0 and gra[x][y-1] == 0 and dis[x-1][y-1][0] == -1:
                dis[x-1][y-1][0] = dis[x][y][d] + 1
                Q.append((x-1, y-1, 0))
                
            if 0 <= x-1 and y+1 < N and gra[x-1][y+1] == 0 and gra[x][y+1] == 0 and dis[x-1][y+1][0] == -1:
                dis[x-1][y+1][0] = dis[x][y][d] + 1
                Q.append((x-1, y+1, 0))
    for d in dis:
        print(d)
