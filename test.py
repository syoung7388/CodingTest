from collections import deque
if __name__ == "__main__":
    M, N = map(int, input().split())
    gra= [list(map(int, input().split())) for _ in range(M)]
    dis= [[[0]*4 for _ in range(N)] for _ in range(M)]
    sx, sy, sd = map(int, input().split())
    ex, ey, ed = map(int, input().split())
    dis[sx-1][sy-1][sd-1] = 1
    Q=deque()
    Q.append((sx-1, sy-1, sd-1,0))
    XY = [[0,1], [0, -1], [0,1], [0,-1]]
    change = [[2,3], [2,3], [0,1], [0,1]]   
    while Q:
        x, y, d , cnt = Q.popleft() 
        if (x,y,d) == (ex-1, ey-1, ed-1):
            print(cnt)
            break
        
        for i in range(1, 4):
            xx, yy = XY[d][0]*i +x, XY[d][1]*i +y
            if not(0<=xx<M and 0<=yy<N) or gra[xx][yy] == 1:
                break
            if dis[xx][yy][d] == 0:
                dis[xx][yy][d] = 1
                Q.append((xx, yy, d, cnt+1))
        for nd in change[d]:
            if dis[x][y][nd] == 0:
                dis[x][y][nd] =1
                Q.append((x, y, nd,cnt+1))
