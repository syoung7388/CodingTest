def BFS(Q, cnt):
    res = 0
    while Q:
        x, y = Q.popleft()
        for i in range(6):
            xx, yy = dx[i]+x, dy[i]+y
            if not (0<=xx<N and 0<=yy<M) or gra[xx][yy] != 0: continue
            if xx//R == x//R or 4 <=i<= 5:
                gra[xx][yy] = gra[x][y]+1
                res = max(res,gra[xx][yy])
                cnt -= 1
                Q.append((xx,yy))
    if cnt == 0:
        return max(res-1, 0)
    else:
        return -1
        
from collections import deque
import sys
input = sys.stdin.readline
M,N,K = map(int, input().split())
R = N
N = N*K
gra = [list(map(int, input().split())) for _ in range(N)]

q = deque()
cnt = 0
for n in range(N):
    for m in range(M):
        if gra[n][m] == 1:
            q.append((n, m))
        elif gra[n][m] == 0:
            cnt += 1

dx, dy = [-1,0,1,0,R,-R],[0,1,0,-1,0,0]

print(BFS(q, cnt))


