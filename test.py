
import sys
input = sys.stdin.readline

xy = [(0, 0), (-1, 0), (-1, -2), (0, -2), (1, -2), (1, 0), (1, 2), (0, 2), (-1, 2)]
def DFS(x, y, d, s, g, f):

    global res
    g = [arr[:] for arr in g]
    n_fish = [arr[:] for arr in f]
    res = max(res, s)
    for a in range(1, 17):
        if not n_fish[a]: continue
        i, j = n_fish[a]
        if g[i][j] == -1 or a == 0: continue
        for k in range(g[i][j+1], g[i][j+1]+8):
            if k > 8: k -= 8
            xx, yy = xy[k][0]+i, xy[k][1]+j
            if not (0<=xx<4 and 0<=yy<8) or g[xx][yy] == -1: continue
            n_fish[g[xx][yy]], n_fish[g[i][j]] = [], []
            g[xx][yy], g[i][j]= g[i][j], g[xx][yy]
            g[xx][yy+1], g[i][j+1] = k, g[xx][yy+1]
            n_fish[g[xx][yy]] = [xx, yy]
            if g[i][j] != 0:         
                n_fish[g[i][j]] = [i, j]

            break
                    
    #상어이동
    g[x][y] = 0
    g[x][y+1] = 0
    #flag = False
    for i in range(1, 5):
        xx, yy = xy[d][0]*i+x, xy[d][1]*i+y
        if not (0<=xx<4 and 0<=yy<8): continue
        if g[xx][yy] == 0: continue
        #flag = True
        die = g[xx][yy]
        die_d = g[xx][yy+1]
        g[xx][yy] = -1
        ns = s+die
        n_fish[die] = []
        DFS(xx, yy, g[xx][yy+1], ns, g, n_fish)
        n_fish[die] = [xx, yy]
        g[xx][yy] = die
        g[xx][yy+1] = die_d\

        


  
    

dx, dy = [0, -1, -1, 0, 1, 1, 1, 0, -1], [0, 0, -2, -2, -2, 0, 2, 2, 2]

gra = [list(map(int, input().split())) for _ in range(4)]

        


fish = [[] for _ in range(17)]

for i in range(4):
    for j in range(0, 8, 2):
        if gra[i][j] > 0:
            fish[gra[i][j]] = [i, j]
        

st = gra[0][0]
fish[gra[0][0]] = []
gra[0][0] = -1
res = 0
DFS(0, 0, gra[0][1],  st, gra, fish)
print(res)
