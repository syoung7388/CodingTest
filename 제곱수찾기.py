
import sys
sys.setrecursionlimit(10**6)


def isS(n):
    return int(n**0.5)**2 == n


def DFS(x, y, i, j,num):
    global res
    if isS(int(num)):
        res = max(res, int(num))

    if 0<=x+i < N and 0<=y+j < M:
        DFS(x+i, y+j, i, j,num+gra[x+i][y+j])

N , M = map(int, input().split())

gra= [list(map(str, input())) for _ in range(N)]

res= -1
for r in range(N): 
    for c in range(M):
        for i in range(-N, N):
            for j in range(-M,M):
                if i == 0 and j == 0: continue
                DFS(r, c, i, j, gra[r][c])
        
        
print(res)
