import sys
input = sys.stdin.readline
import heapq
from collections import deque
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


def find(i, j):
    ch = [[0]*N for _ in range(N)]
    H =[(0, i, j)]
    ch[i][j] = 1
    
    while H:
        v, x, y = heapq.heappop(H)
        if gra[x][y] > 1: 
            return [v, x, y]
        
        for k in range(4):
            xx, yy = dx[k]+x, dy[k]+y
            if not (0<=xx<N and 0<=yy<N) or gra[xx][yy] == 1: continue
            if ch[xx][yy] == 0:
                ch[xx][yy] = 1
                heapq.heappush(H, (v+1, xx, yy))

                
    return False    
            
def ride(n, d, i, j):
    global F, x, y
    
    F -= d
    if F < 0:
        return False
    
    Q = deque([(i, j)])
    ch = [[-1]*N for _ in range(N)]
    ch[i][j] = 0
    
    while Q:
        a, b = Q.popleft()
        if a == end[n][0] and b == end[n][1]:
            F -= ch[a][b]
            x, y = a, b
            if F >= 0: 
                F += ch[a][b]*2
                return True
            return False
        for k in range(4):
            xx, yy = dx[k]+a, dy[k]+b
            if not (0<= xx < N and 0<=yy<N) or gra[xx][yy] == 1: continue
            if ch[xx][yy] == -1:
                ch[xx][yy] = ch[a][b]+1
                Q.append((xx, yy))
                
    return False    
    
    
    


N, M, F = map(int, input().split())
gra = [list(map(int, input().split())) for _ in range(N)]
x, y = map(int, input().split())
x, y = x-1, y-1

start = {}
end = {}
for i in range(2, M+2):
    sx, sy, ex, ey = map(int, input().split())
    start[i] = [sx-1, sy-1]
    gra[sx-1][sy-1] = i
    end[i] = [ex-1, ey-1]
res = False  
for _ in range(M):
    arr = find(x, y)
    if not arr:
        res = True
        break
    
    d, sx, sy = arr
    n = gra[sx][sy]
    gra[sx][sy] = 0
    
    if not ride(n, d, sx, sy): 
        res = True
        break

    
if res:
    print(-1)
    
else:
    print(F)
