


import sys

input = sys.stdin.readline


def CheckCnt(xx, yy):
    bf = 0
    row = gra[0][yy]
    rowcnt = 0
    col = gra[xx][0]
    colcnt = 0
    for k in range(N):
        if row == gra[k][yy]:
            rowcnt += 1
            bf = max(bf, rowcnt)
        else:
            row= gra[k][yy]
            rowcnt = 0

            
        if col == gra[xx][k]:
            colcnt += 1
            bf = max(bf, colcnt)
        else:
            col = gra[xx][k]
            colcnt = 0
    return bf
            
            
            
        


N = int(input())
gra = [list(map(str, input())) for _ in range(N)]

Maxcnt = list()

dx = [-1, 0]
dy = [0, 1]
for i in range(N):
    for j in range(N):
        for l in range(2):
            x = dx[l]+i
            y = dy[l]+j
            gra[x][y],gra[i][j] = gra[i][j],gra[x][y]
            Maxcnt.append(CheckCnt(x, y))
            Maxcnt.append(CheckCnt(i, j))
            gra[x][y],gra[i][j] = gra[i][j],gra[x][y]
print(max(Maxcnt))
                

                


            
            
