dx, dy = [-1,-1,-1,0,0,1,1,1], [-1, 0, 1, -1, 1, -1, 0, 1]

def DFS(x, y):
    global flag
    ch[x][y] = 1
    for k in range(8):
        xx, yy = dx[k]+x, dy[k]+y
        if not (0<= xx< N and 0<=yy<M):continue
        if gra[x][y] < gra[xx][yy]:
            flag = False
          
        if gra[xx][yy] == gra[x][y] and ch[xx][yy] == 0:
            DFS(xx, yy)
N, M = map(int, input().split())
gra = [list(map(int, input().split())) for _ in range(N)]
ch = [[0]*M for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        if ch[i][j] == 0 and gra[i][j] > 0:
            flag = True
            DFS(i, j)
            if flag:
                cnt += 1
print(cnt)
