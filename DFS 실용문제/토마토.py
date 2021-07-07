from collections import deque


if __name__ == "__main__":
    M, N = map(int, input().split()) #M=>열 #N=>행
    gra = [list(map(int, input().split())) for _ in range(N)]
    ch = [[0]*M for _ in range(N)]
    dQ = deque()
    for n in range(N):
        for m in range(M):
            if gra[n][m] == 1:
                dQ.append((n,m))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0
    while dQ:
        qx, qy = dQ.popleft()
        for i in range(4):
            x = qx +dx[i]
            y = qy +dy[i]
            if 0 <= x < N and 0 <= y < M and gra[x][y]==0:
                gra[x][y] = 1
                ch[x][y] = ch[qx][qy] +1
                dQ.append((x,y))
                cnt = max(cnt, ch[x][y])
    flag = 1
    for a in range(N):
        for b in range(M):
            if gra[a][b] == 0:
                flag = 0
    if flag == 1:
        print(cnt)
    else:
        print(-1)
       
