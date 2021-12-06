import sys
input = sys.stdin.readline

dx, dy = [0, -1, 1, 0, 0], [0, 0, 0, -1, 1]
def move(pos):
    for n, x, y, d in pos:
        smell[x][y] = [n, K]
    
    n_pos = []
    
    for n, x, y, d in pos:
        if gra[x][y] == n:
            gra[x][y] = 0
        my = []
        for k in turn[n][d]:
            xx, yy = dx[k]+x, dy[k]+y
            if not (0<=xx<N and 0<=yy<N): continue
            if smell[xx][yy][0] == 0:
                if (gra[xx][yy] != 0 and gra[xx][yy] > n) or gra[xx][yy] == 0:
                    gra[xx][yy] = n
                    n_pos.append([n, xx, yy, k])
                break
            if not my and smell[xx][yy][0] == n:
                my = [xx, yy, k]
        else:
            if my :
                gra[my[0]][my[1]] = n
                n_pos.append([n, my[0], my[1], my[2]])
    for i in range(N):
        for j in range(N):
            if smell[i][j] == 0: continue
            smell[i][j][1] -= 1
            if smell[i][j][1] <= 0:
                smell[i][j] = [0, 0]
                
    return n_pos            
            
    
N, M, K = map(int, input().split())
gra = [list(map(int, input().split())) for _ in range(N)]
direct = list(map(int, input().split()))
turn = [[0] for _ in range(M+1)]
for i in range(M*4):
    turn[i//4+1].append(list(map(int, input().split())))

pos = []
for i in range(N):
    for j in range(N):
        if gra[i][j] == 0: continue
        pos.append([gra[i][j], i, j, direct[gra[i][j]-1]])
smell = [[[0, 0] for _ in range(N)] for _ in range(N)]
        
pos.sort()
sec = 0
for _ in range(1000):
    pos = move(pos)
    pos.sort()
    sec += 1
    if pos[0][0] != 1:break
    if len(pos) == 1: break

if len(pos) == 1 and pos[0][0] == 1:
    print(sec)
else:
    print(-1)
    
