import sys
input = sys.stdin.readline
from itertools import combinations

def check_dfs(x, y,ng,ch):
    for garo, sero in ng[y]:
        if garo >= x and not (garo, y, sero) in ch:
            ch.add((garo, sero, y)) 
            return check_dfs(garo, sero,ng, ch)
    return y

def check(g):
    ng = [sorted(a[:]) for a in g]
    for i in range(1, N+1):
        arr = check_dfs(1, i,ng, set())
        if arr != i:
            return False
    return True

M, H, N = map(int, input().split())


G = [[] for _ in range(N+1)] #a(출발세로선) ->b(도착세로선) #가로선은 v
gra = [[0]*(M+1) for _ in range(N+1)]                            #G [b] -> [(v, b+1)]

for _ in range(H):
    a, b = map(int, input().split())
    G[b].append((a, b+1))
    G[b+1].append((a, b))
    gra[a][b] = 1
    gra[a][b+1] = 1

road = []
for i in range(1, N+1):
    for j in range(1, M):
        if gra[i][j] == 0 and gra[i][j+1] == 0:
            road.append((i, j, j+1))

    
res = 2147000000

for com in combinations(road, 1):
    nG = [g[:] for g in G]
    for a, b1, b2 in road:
        nG[b1].append((a, b2))
        nG[b2].append((a, b1))
    if check(nG):
        print(1)
        sys.exit(0)

for com in combinations(road, 2):
    
    nG = [g[:] for g in G]
    for a, b1, b2 in road:
        nG[b1].append((a, b2))
        nG[b2].append((a, b1))
    if check(nG):
        print(2)
        sys.exit(0)    

for com in combinations(road, 3):
    
    nG = [g[:] for g in G]
    for a, b1, b2 in road:
        nG[b1].append((a, b2))
        nG[b2].append((a, b1))
    if check(nG):
        print(3)
        sys.exit(0)    
print(-1)
            
            
