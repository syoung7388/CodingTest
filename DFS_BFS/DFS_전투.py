
def DFS(x, y, team):
    global num
    gra[x][y] =0
    num += 1
    for k in range(4):
        xx = x+dx[k]
        yy = y+dy[k]
        if 0<=xx<M and 0<=yy<N and gra[xx][yy]==team:
            DFS(xx, yy, team)


if __name__ == "__main__":
    N, M = map(int, input().split())
    gra = [list(map(str, input())) for _ in range(M)]
    dx = [-1, 0, 1, 0]
    dy= [0, 1, 0, -1]
    my = 0
    you = 0
    for i in range(M):
        for j in range(N):
            num = 0
            if gra[i][j] == 'W':
                DFS(i,j,'W')
                my += num**2
            elif gra[i][j] == 'B':
                DFS(i,j,'B')
                you += num**2

    print(my, you)
