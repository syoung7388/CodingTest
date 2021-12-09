import sys
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10**5)
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def Turn(n):


    melt = defaultdict(int)

    n_gra = [[0]*N for _ in range(N)]
    for i in range(0, N, n):
        for j in range(0, N, n):
            for x in range(i, i+n):
                for y in range(j, j+n):
                    a, b = y+i-j, n - (x-i-j+1)
                    n_gra[a][b] = gra[x][y]
                    if n_gra[a][b] != 0: continue
                    for k in range(4):
                        xx, yy = dx[k]+a, dy[k]+b
                        if not (0<=xx<N and 0<=yy<N): continue
                        melt[(xx, yy)] += 1
    melt[(0,0)] = 1
    melt[(0,N-1)] = 1
    melt[(N-1,0)] = 1
    melt[(N-1,N-1)] = 1
    return n_gra, melt
                        
                    
                    

def melting(melt):
    for k , v in melt.items():
        if (k[0] == 0 or k[0] == N-1 or k[1] == 0 or k[1] == N-1) and v>=1:
            if gra[k[0]][k[1]] == 0: continue
            gra[k[0]][k[1]] -= 1
        elif v >= 2:
            if gra[k[0]][k[1]] == 0: continue
            gra[k[0]][k[1]] -= 1
    

def DFS(x, y):
    res = 1
    gra[x][y] = 0
    for k in range(4):
        xx, yy = dx[k]+x, dy[k]+y
        if not (0<=xx<N and 0<=yy<N) or gra[xx][yy] == 0: continue
        res += DFS(xx, yy)
    return res

#main
N, Q = map(int, input().split())
N = 2**N
gra = [list(map(int, input().split())) for _ in range(N)]


for t in list(map(int, input().split())):
    gra, melt = Turn(2**t)
    melting(melt)



print(sum(sum(g) for g in gra))
result = 0
for i in range(N):
    for j in range(N):
        if gra[i][j] != 0:
            result = max(DFS(i, j), result)

print(result)
    
