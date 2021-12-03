import sys
input = sys.stdin.readline
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
turn = [1, 0, 3, 2]
def Move(h):

    x, y, d = pos[h]
    xx, yy = x+dx[d], y+dy[d] #이동칸


    if not (0<=xx<N and 0<=yy<N) or gra[xx][yy] == 2:
        d = turn[d]
        xx, yy = x+dx[d], y+dy[d]
        if not (0<=xx<N and 0<=yy<N) or gra[xx][yy] == 2:
            pos[h][2] = d
            return False
        
    arr = []
    while True:
        arr.append(G[x][y].pop())
        if arr[-1] == h: break

    if gra[xx][yy] == 0:
        arr.reverse()
        
    for a in arr:
        G[xx][yy].append(a)
        pos[a][0] = xx
        pos[a][1] = yy

    pos[h][2] = d
    if len(G[xx][yy]) >= 4:
        return True
    return False
    

N, K = map(int, input().split())
gra = [list(map(int, input().split())) for _ in range(N)]
G = [[[] for _ in range(N)] for _ in range(N)]
pos = [[] for _ in range(K+1)]
for i in range(1, K+1):
    x, y, d = map(int, input().split())
    pos[i] = [x-1, y-1, d-1]
    G[x-1][y-1].append(i)


for r in range(1, 1001):

    for i in range(1, K+1):
        if Move(i):
            print(r)
            sys.exit(0)
            
print(-1)
