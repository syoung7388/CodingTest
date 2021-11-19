import sys
input = sys.stdin.readline
from itertools import product


def Row():
    global Max

    row = [[[] for _ in range(10)] for _ in range(6)]
    #row_sum = [[0]*10 for _ in range(6)]
    for i in range(6):
        a, b, c, d, e, f = bro[i][0], bro[i][1], bro[i][2], bro[i][3], bro[i][4], bro[i][5]
        for j in range(10): 
            row[i][j] = [a, b, c, d, e, f]
            row_sum[i][j] =a+b+c+d+e+f 
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

            
    for per in product(range(10), repeat = 6): #151200
        R = []
        for idx, p in enumerate(per):
            R.append(row[idx][p])
            Col(R)
def Col(gra):
    col = [[[] for _ in range(10)] for _ in range(6)]
    col_sum = [[0]*10 for _ in range(6)]
    max_sum = 0
    for i in range(6):
        a, b, c, d, e, f = gra[0][i], gra[1][i], gra[2][i], gra[3][i], gra[4][i], gra[5][i]
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
        if s > max_sum:
            C = per
            Max = s
      

    if C:
        for i in range(6):
            for j in range(6):
                gra[j][i] = col[i][C[i]][j]
def Dia():
    global Max


    
    a, b, c, d, e, f = gra[0][0], gra[1][1], gra[2][2], gra[3][3], gra[4][4], gra[5][5]
    mf = Max - (a+b+c+d+e+f)
    for i in range(10):
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
        s = a+b+c+d+e+f

        S = mf + s
        if S >Max:
            Max = S
            gra[0][0], gra[1][1], gra[2][2], gra[3][3], gra[4][4], gra[5][5] = a, b, c, d, e, f
            
    a, b, c, d, e, f = gra[0][5], gra[1][4], gra[2][3], gra[3][2], gra[4][1], gra[5][0]
    mf = Max - (a+b+c+d+e+f)
    for i in range(10):
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
        s = a+b+c+d+e+f
        S = mf + s
        if S > Max:
            Max = S
            gra[0][5], gra[1][4], gra[2][3], gra[3][2], gra[4][1], gra[5][0] = a, b, c, d, e, f    


    
cnt = 0
bro = [list(map(int, input().split())) for _ in range(6)]



