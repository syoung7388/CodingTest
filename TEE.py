import sys
input= sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import defaultdict
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


def Turn(i, j, a, b, n):
    for x in range(i, i+n):
        for y in range(j, j+n):
            nx, ny = y-a+b, n-(x+a+b+1)
            n_gra[nx][ny] = gra[x][y]
            if n_gra[nx][ny] <= 0:
                for k in range(4):
                    xx, yy = nx+dx[k], ny+dy[k]
                    if not (0<=xx<N and 0<=yy<N): continue
                    melt[(xx, yy)] += 1
           
                        
               

                
def DFS(x, y):
    global cnt
    ch[x][y] = 1
    cnt += 1
    for k in range(4):
        xx, yy = dx[k]+x, dy[k]+y
        if not (0<=xx<N and 0<=yy<N) or ch[xx][yy] == 1: continue
        if gra[xx][yy] > 0:
            DFS(xx, yy)
    
    
N, Q = map(int, input().split())
N = 2**N
gra = [list(map(int, input().split())) for _ in range(N)]
T = list(map(int, input().split()))
arr = [(0, 0), (0, N-1), (N-1, 0), (N-1, N-1)]

for t in T:
    n = 2**t
    n_gra = [g[:] for g in gra]
    melt = defaultdict(int)
    for i in range(0, N, n):
        for j in range(0, N, n):
            Turn(i, j, -i, -j, n)

    for k, v in melt.items():
     
        if k in arr: continue
        if (k[0] == 0 or k[0] == 7 or k[1] == 7 or k[1] == 0) and v >= 1:
            n_gra[k[0]][k[1]] -= 1
        elif v >= 2:
            n_gra[k[0]][k[1]] -= 1
            
    for ax, ay in arr:
        n_gra[ax][ay] -= 1  
    gra = n_gra



ch = [[0]*N for _ in range(N)]
res1 = 0
res2 = 0
for i in range(N):
    for j in range(N):
        if gra[i][j] <= 0: continue
        res1+=gra[i][j]
        if ch[i][j] == 1: continue
        cnt = 0
        DFS(i, j)
        res2 = max(res2, cnt)


print(res1)
print(res2)
