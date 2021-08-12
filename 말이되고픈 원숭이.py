from collections import deque
import sys
input = sys.stdin.readline

K = int(input())
W, H = map(int, input().split())
gra = [list(map(int, input().split())) for _ in range(H)]
dis = [[[0]*(K+1) for _ in range(W)] for _ in range(H)]
#-1,0,1,0 // 0,1,0,-1
m = [[-1, 0],[0,1], [1, 0], [0,-1]]
c = [[-2, -1], [-1,-2], [-2, 1], [-1,2], [1, 2], [2,1], [1, -2], [2, -1]]

def Move(sx, sy):
    global K
    Q = deque([(sx, sy, 0)])

    while Q:
        x, y, cnt = Q.popleft()
        if (x, y) == (H-1, W-1):
            return dis[x][y][cnt]

        #원숭이 이동법
        for k in range(4):
            xx, yy = m[k][0]+x, m[k][1]+y
            if not (0<=xx<H and 0<=yy<W) or gra[xx][yy] == 1: continue
            if dis[xx][yy][cnt] == 0:
                dis[xx][yy][cnt] = dis[x][y][cnt]+1
                Q.append((xx, yy, cnt))
        if cnt == K: continue
        # 말이동법
        for i in range(8):
            xx, yy = c[i][0]+x, c[i][1]+y
            if not(0<=xx<H and 0<=yy<W) or gra[xx][yy] == 1: continue
            if dis[xx][yy][cnt+1] == 0:
                dis[xx][yy][cnt+1] = dis[x][y][cnt]+1
                Q.append((xx, yy, cnt+1))

    return -1


print(Move(0,0))
