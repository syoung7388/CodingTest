


  
import sys
sys.setrecursionlimit(10**6)


def DFS(x, y, h):
    ch[x][y] = 1
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<N and 0<=yy<N and gra[xx][yy]>h and ch[xx][yy] == 0:
            DFS(xx,yy,h)

if __name__ == "__main__":
    N = int(input())
    gra = [list(map(int, input().split())) for _ in range(N)]
    dx = [-1,0,1,0]
    dy=[0,1,0,-1]
    bf = -1
    for h in range(1,101):
        cnt = 0
        ch =[[0]*N for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if ch[i][j] == 0 and gra[i][j] > h:
                    cnt += 1
                    DFS(i, j, h)
        if cnt == 0:
            break
        if cnt > bf:
            bf = cnt
    print(bf)
