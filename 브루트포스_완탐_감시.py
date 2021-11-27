import sys
input = sys.stdin.readline



def DFS(L, ch):
    global res
    if L == C:
        res = max(len(ch), res)
        return

    x, y = cctv[L]
    for i in dic[gra[x][y]]:
        arr = set()
        for j in i:
            xx, yy = dx[j]+x, dy[j]+y
            while True:
                if not (0<=xx<N and 0<=yy<M) or gra[xx][yy] == 6: break
                if gra[xx][yy] == 0:
                    arr.add((xx, yy))
                xx += dx[j]
                yy += dy[j]
        DFS(L+1, ch|arr)

    
N, M = map(int, input().split())
gra = [list(map(int, input().split())) for _ in range(N)]

cctv = []
cnt  = 0
for i in range(N):
    for j in range(M):
        if 1<= gra[i][j]<= 5:
            cctv.append((i, j))
        if gra[i][j] == 0:
            cnt += 1
            
            
dx, dy = [0, 1, 0, -1] , [1, 0, -1, 0]

dic = {1:[[0], [1], [2], [3]], 2:[[0, 2], [1, 3]], 3:[[0, 3], [0,1], [1, 2], [2, 3]], 4:[[0, 2, 3], [0, 1, 3], [0, 1, 2], [1, 2, 3]], 
      5:[[0, 1, 2, 3]]}

C = len(cctv)
res = 0
DFS(0, set())

print(cnt - res)
