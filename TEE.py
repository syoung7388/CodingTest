import sys
input = sys.stdin.readline
from itertools import product
def PickCol(G):
    global Max
    col = [[[] for _ in range(10)] for _ in range(6)]
    col_sum = [[0]*10 for _ in range(6)]
    for i in range(6):
        a, b, c, d, e, f = G[0][i], G[1][i], G[2][i], G[3][i], G[4][i], G[5][i]
        for j in range(10): #60
            col[i][j] = [a, b, c, d, e, f]
            col_sum[i][j] =a+b+c+d+e+f 
            a += 1
            b += 1
            c += 1
            d += 1
            e += 1
            f += 1
            if a == 10: a=0
            if b == 10: b=0
            if c == 10: c=0
            if d == 10: d=0
            if e == 10: e=0
            if f == 10: f=0
    C = []
    for per in  product(range(10), repeat = 6): #1000000
        s = 0
        for idx, p in enumerate(per):
            s += col_sum[idx][p]
        if s > Max:
            C = per
            Max = s
            
    
    if C:
        for i in range(6):
            for j in range(6):
                
                G[j][i] = col[i][C[i]][j]
                
    return G

N = 6
gra = [list(map(int, input().split())) for _ in range(N)]

Max = 0

row = [[[0]*6 for _ in range(10)] for _ in range(N)]


for i in range(N):
    row[i][0] = gra[i]



for i in range(N):
    for j in range(1,10):
        for a in range(N):
            row[i][j][a]  = row[i][j-1][a] + 1
            if row[i][j][a] == 10:
                row[i][j][a] = 0



for pro in product(range(10), repeat = 6):
    G = []
    for idx, p in enumerate(pro):
        G.append(row[idx][p])

    gra = PickCol(G)
