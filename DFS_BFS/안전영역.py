import sys
sys.setrecursionlimit(10**6)
def DFS(x, y, h):
    dis[x][y] = 1
    for l in range(4):
        xx= x+dx[l]
        yy = y+dy[l]
        if 0 <= xx < N and 0 <= yy < N and dis[xx][yy] == 0 and gra[xx][yy] > h:
            DFS(xx, yy, h)

if __name__ == "__main__":
    N = int(input())
    gra = [list(map(int, input().split())) for _ in range(N)]
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    res = 0

    for h in range(100):
        cnt = 0
        dis = [[0]*(N) for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if dis[i][j] == 0 and gra[i][j] > h:
                    cnt += 1
                    DFS(i, j, h)
        res = max(res, cnt)
        if cnt == 0:
            break
    print(res)
    
    
  
