import sys
input = sys.stdin.readline

N = int(input())
gra = [[0]*(101) for _ in range(101)]
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]


for k in range(N):
    y, x, d, g = map(int, input().split())
    gra[x][y] = 1
    curve = [d]
    for j in range(g):
        for k in range(len(curve)-1, -1, -1):
            curve.append((curve[k]+1)%4)
    for i in range(len(curve)):
        x += dx[curve[i]]
        y += dy[curve[i]]

        if not (0<=x<101 and 0<=y<101): continue

        gra[x][y] = 1
res = 0
for i in range(101):
    for j in range(101):
        if gra[i][j] == 1 and gra[i+1][j] == 1 and gra[i][j+1] == 1 and gra[i+1][j+1] == 1:
            res += 1
print(res)

""" 90도 회전하고 기준점으로 끌어올리기
import sys
input = sys.stdin.readline
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]



def curve():
    global ex, ey
    
    a = - min(X)
    b = -min(Y)
    n =  max(X) - min(X) + 1
    i, j = ex - (ey + b -a), ey - (n -(ex+a+b+1)) #끝점이 이동하는 임시점
    ex, ey = (sy+b-a)+i, n-(sx+a+b+1)+j
    temp = set()
    for x, y in arr:
        xx, yy = (y+b-a)+i, n-(x+a+b+1)+j
        if not (0<=xx<M+1 and 0<=yy<M+1): return False        
        X.add(xx)
        Y.add(yy)
        temp.add((xx, yy))
    return  temp 
    
    

N = int(input())
M = 100
gra = [[0]*(M+1) for _ in range(M+1)]
min_x, max_x = 101, 0
min_y, max_y = 101, 0
for _ in range(N): 
    sy, sx, d, g = map(int, input().split())
    ex, ey = sx +dx[d], sy+dy[d]
    gra[sx][sy] = 1
    gra[ex][ey] = 1

    
    X = set([sx, ex])
    Y = set([sy, ey])
    arr = set([(sx, sy), (ex, ey)])
    flag = False
    for a in range(1, g+1): 
        n_arr = curve()
        if not n_arr:break
        arr |=n_arr
    else:
        min_x, max_x= min(min_x, min(X)), max(max_x, max(X))
        min_y, max_y= min(min_y,  min(Y)), max(max_y, max(Y))
        for ax, ay in arr:
            gra[ax][ay] = 1


res = 0
for i in range(min_x, max_x+1):
    for j in range(min_y,max_y+1):
        if gra[i][j] == 1:
            if gra[i][j+1] ==1 and gra[i+1][j] == 1 and gra[i+1][j+1] == 1:
                res += 1

print(res)
    

"""
