def DFS(x, y):
    global home
    gra[x][y] = 0
    home+=1
    for k in range(4):
        xx = dx[k]+x
        yy = dy[k]+y
        if 0<=xx<N and 0<=yy<N and gra[xx][yy]==1:
            DFS(xx, yy)

if __name__ == "__main__":
    N = int(input())
    gra = [list(map(int, input())) for _ in range(N)]
    home=0
    homes = []
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    for i in range(N):
        for j in range(N):
            if gra[i][j] == 1:
                DFS(i, j)
                homes.append(home)
                home=0
    print(len(homes))
    for h in homes:
        print(h)
