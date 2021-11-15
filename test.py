from collections import deque
import sys
n, m = map(int, input().split())
gra = [list(map(str, input())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if gra[i][j] == '0':
            sx, sy = i, j
            break
            
Q = deque([(sx, sy, 1<<7)])
dis = [[[-1]*(1<<7+1) for _ in range(m)] for _ in range(n)]
dis[sx][sy][1<<7] = 0

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
while Q:
    x, y, key = Q.popleft()
    
    for k in range(4):
        xx, yy = dx[k]+x, dy[k]+y
        if not (0<=xx<n and 0<=yy<m) : continue
        if gra[xx][yy] == '#': continue
        if gra[xx][yy] == '1':
            print(dis[x][y][key]+1)
            sys.exit(0)        
        n_key = key
        o = ord( gra[xx][yy])
        if "A" <= gra[xx][yy] <= "F" and key & (1<<(o-65)) == 0: continue
        if "a" <= gra[xx][yy] <= 'f':
            n_key |= (1<<(o-97))
            
        if dis[xx][yy][n_key] != -1: continue
        dis[xx][yy][n_key] = dis[x][y][key] + 1
        Q.append((xx, yy, n_key))
print(-1)
            
