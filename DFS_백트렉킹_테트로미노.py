import sys
input = sys.stdin.readline
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
def DFS(L, x, y, s):
    global res

    if res - s >= 1000 * (4 - L):
        return    
    if L == 4:
        res = max(res, s)
        return
    
    for k in range(4):
        xx, yy = dx[k]+x, dy[k]+y
        if not (0<=xx<N and 0<=yy<M) or ch[xx][yy] == 1: continue
        ch[xx][yy] = 1
        if L == 2:
            DFS(L+1, x, y, s + gra[xx][yy])
        DFS(L+1, xx, yy, s+gra[xx][yy])        
        ch[xx][yy] = 0
        

N, M = map(int, input().split())
gra = [list(map(int, input().split())) for _ in range(N)]

ch = [[0]*(M) for _ in range(N)]
res = 0
for i in range(N):
    for j in range(M):
        ch[i][j] = 1
        DFS(1, i, j,gra[i][j])
        ch[i][j] = 0


print(res)

