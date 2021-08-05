from collections import deque
import sys
def BFS(i, j, visit):
    Q = deque([(i, j)])
    visit[i][j] = 1
    melQ = deque()
    while Q:
        x, y = Q.popleft()
        melcnt = 0
        for k in range(4):
            xx= x+dx[k]
            yy = y+dy[k]
            if 0<=xx<N and 0<=yy<M and visit[xx][yy] == 0:
                if gra[xx][yy] != 0:                    
                    visit[xx][yy]= 1
                    Q.append((xx, yy))
                if gra[xx][yy] ==0:
                    melcnt += 1
        if melcnt >= 0:
            melQ.append([x, y, melcnt])
    return melQ

input = sys.stdin.readline
year = 0
N, M = map(int, input().split())
gra = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
while True:
    cnt = 0
    
    visit = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if gra[i][j] != 0 and visit[i][j] == 0:
                cnt += 1
                melT = BFS(i, j, visit)
                while melT:
                    mx, my, m = melT.popleft()
                    gra[mx][my] = max(gra[mx][my]-m, 0)
    if cnt == 0:
        year = 0
        break
    if cnt >= 2:
        break
    year += 1
print(year)
