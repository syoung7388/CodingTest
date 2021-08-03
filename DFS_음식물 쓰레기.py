def DFS(x,y):
    global num
    num += 1
    gra[x][y] = 0
    for k in range(4):
        xx = x+dx[k]
        yy = y+dy[k]
        if 0<=xx<N and 0<=yy<M and gra[xx][yy] == 1:
            DFS(xx, yy)
if __name__ == "__main__":
    N, M, K = map(int, input().split())
    gra = [[0]*M for _ in range(N)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for _ in range(K):
        x, y = map(int,input().split())
        gra[x-1][y-1]=1
    MaxNum = -1
    num = 0
    for i in range(N):
        for j in range(M):
            if gra[i][j] == 1:    
                DFS(i, j)
                MaxNum = max(num, MaxNum)
                num=0
    print(MaxNum)            
        
