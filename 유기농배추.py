

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
def DFS(x, y):
    gra[x][y] = 0
    for k in range(4):
        xx, yy = dx[k]+x, dy[k]+y
        if not (0<=xx<N and 0<=yy<M): continue
        if gra[xx][yy] == 1:
            DFS(xx, yy)



for _ in range(int(input())):
    M, N, K= map(int, input().split())
    gra = [[0]*(M) for _ in range(N)]

    for _ in range(K):
        a, b = map(int, input().split())
        gra[b][a] = 1
    res = 0
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    for i in range(N):
        for j in range(M):
            if gra[i][j] == 1:
                res += 1
                DFS(i, j)
    print(res)           


    
    
    
