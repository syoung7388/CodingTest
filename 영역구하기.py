
def DFS(x, y):
    global num
    gra[x][y] = 1
    num += 1

    for k in range(4):
        xx = x + dx[k]
        yy = y + dy[k]
        if not(0<=xx<M and 0<=yy<N) or gra[xx][yy] == 1:
            continue
        DFS(xx, yy)
            
if __name__ == "__main__":
    N, M, K = map(int, input().split())
    dx, dy = [-1, 0, 1, 0], [0,1,0,-1]

    gra = [[0]*N for _ in range(M)]
    for _ in range(K):
        a1, a2, b1, b2 = map(int, input().split())
        for i in range(a1, b1):
            for j in range(a2, b2):
                gra[i][j] = 1

    res = list()
    num = 0
    for a in range(M):
        for b in range(N):
            if gra[a][b] == 0:
                DFS(a, b)
                res.append(num)
                num = 0
    print(len(res))
    for r in sorted(res):
        print(r, end=" ")
    
