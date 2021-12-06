
def move(arr, t, gra):
    global sc
    r = 5
    for ax, ay in arr:
        for i in range(6):
            if gra[i][ay] == 1:
                r = min(r, i-1)
                break
    if t == 1:
        gra[r][arr[0][1]] = 1
    elif t == 2:
        gra[r][arr[0][1]] = 1
        gra[r][arr[1][1]] = 1
    elif t == 3:
        gra[r-1][arr[0][1]] = 1
        gra[r][arr[1][1]] = 1
    for i in range(6):
        for j in range(4):
            if gra[i][j] == 0:
                break
        else:
            sc += 1
            gra.pop(i)
            gra = [[0]*4]+gra
            
        
     
    return gra
def check():
    global g, b
    for i in range(2):
        fb = False
        fg = False
        for j in range(4):
            if g[i][j] == 1:
                fg = True
            if b[i][j] == 1:
                fb = True
        if fg:
            g.pop()
            g = [[0]*4] + g
        if fb:
            b.pop()
            b = [[0]*4]+b
g = [[0]*4 for _ in range(6)]
b = [[0]*4 for _ in range(6)]
N = int(input())
sc = 0
for _ in range(N):
    t, x, y = map(int, input().split())
    if t == 1:
        g = move([(x, y)], 1, g)
        b = move ([(y, x)], 1, b)
    elif t == 2:
        g = move([(x, y), (x, y+1)], 2, g)
        b = move([(y, x), (y+1, x)], 3, b)
    elif t == 3:
        g = move([(x, y), (x+1, y)], 3, g)
        b = move([(y, x), (y, x+1)], 2, b)
    check()
print(sc)
res = 0


for i in range(6):
    for j in range(4):
        if g[i][j] == 1:
            res += 1
        if b[i][j] == 1:
            res += 1
print(res)
