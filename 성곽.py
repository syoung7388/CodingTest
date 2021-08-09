import sys
sys.setrecursionlimit(10**6)
def make_dy():
    dy[1] = [1]
    dy[2] = [2]
    dy[4] = [4]
    dy[8] = [8]
    for i in range(1, 16):
        if len(dy[i]) == 0:
            for j in range(i, 1, -1):
                if j in (1, 2, 4, 8):
                    dy[i] += dy[i-j]
                    dy[i].append(j)
                    break

def DFS(x, y):
    global cnt
    cnt += 1
    ch[x][y] = R
    for k in xy.keys():
        if k not in dy[gra[x][y]]:
            xx = xy[k][0] + x
            yy = xy[k][1] + y
            if 0<=xx<M and 0<=yy<N and ch[xx][yy] == 0:
                DFS(xx, yy)
if __name__ == "__main__":
    N, M = map(int, input().split())
    gra = [list(map(int, input().split()))  for _ in range(M)]
    dy = [[] for _ in range(16)]
    make_dy()
    xy = {1:[0,-1], 2:[-1,0], 4:[0,1],8:[1,0]}
    bang = list()
    ch=[[0]*(N) for _ in range(M)]
    cnt = 0
    R = 0
    for i in range(M):
        for j in range(N):
            if ch[i][j] == 0:
                R += 1
                DFS(i, j)
                bang.append(cnt)
                cnt = 0
    print(len(bang))
    print(max(bang))
    res = 0


    for a in range(M):
        for b in range(N):
            for k in xy.keys():
                xx , yy = a+xy[k][0], b+xy[k][1]
                if 0<=xx<M and 0<=yy<N and ch[xx][yy] != ch[a][b]:
                    res = max(bang[ch[xx][yy]-1]+bang[ch[a][b]-1], res)
    print(res)

            
        

    
