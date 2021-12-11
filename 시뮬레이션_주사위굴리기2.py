import sys
input = sys.stdin.readline
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
turn = [2, 3, 0, 1]

c = [1, 2, 3, 0]
r = [3, 0, 1, 2]

def Go(n):
    if n == 0:
        return [z[2], z[1], z[5], z[0], z[4], z[3]]
    elif n == 1:
        return [z[4], z[0], z[2], z[3], z[5], z[1]] 
    elif n == 2:
        return [z[3], z[1], z[0], z[5], z[4], z[2]]
    elif n == 3:
        return [z[1], z[5], z[2], z[3], z[0], z[4]]

def DFS(x, y):
    count[x][y] = 1
    arr.append((x, y))
    for k in range(4):
        xx, yy = dx[k]+x, dy[k]+y
        if not (0<=xx<N and 0<=yy<M) or count[xx][yy] != 0: continue
        if gra[xx][yy] == gra[x][y]:
            DFS(xx, yy)
    

z = [1, 5, 4, 3, 2, 6]

N, M, K = map(int, input().split())

gra = [list(map(int, input().split())) for _ in range(N)]
count = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if count[i][j] == 0:
            arr = []
            DFS(i, j)
            n = len(arr)
            if n != 1:
                for ax, ay in arr:
                    count[ax][ay] = n
d = 0
sc = 0
x, y = 0, 0
for i in range(K):
    #1)주사위 이동
    xx, yy = dx[d]+x, dy[d]+y
    if not (0<=xx<N and 0<=yy<M):
        d= turn[d]
        xx, yy = dx[d]+x, dy[d]+y
    z = Go(d)

    #2) 점수
    sc += gra[xx][yy]*count[xx][yy]


    #3) 방향정하기
    if z[-1] > gra[xx][yy]:
        d  = c[d]
    elif z[-1] < gra[xx][yy]:
        d = r[d]
    x, y = xx, yy

        
print(sc)
    
