import sys
input = sys.stdin.readline
from collections import defaultdict
dx, dy =[0, 0, 0, -1, 1], [0, 1, -1, 0, 0]

def within(x, y):
    if not (0<=x<N and 0<=y<M):
        return False
    return True
    
def next_wind(x, y, d):
    if d == 1:
        return [(x-1, y+1), (x, y+1), (x+1, y+1)]
    elif d == 2:
        return [(x-1, y-1), (x, y-1), (x+1, y-1)]
    elif d == 3:
        return [(x-1, y-1), (x-1, y), (x-1, y+1)]
    elif d == 4:
        return [(x+1, y-1), (x+1, y), (x+1, y+1)]
    
    

def on(i, j, d):
    if not within(i, j): return
    wind = [(i, j)]
    up = defaultdict(int)
    up[(i, j)] += 5
    for k in range(4, 0, -1):
        n_wind = []
        for x, y in wind:
            for idx, pos in enumerate(next_wind(x, y, d)):
                xx, yy = pos
                if not within(xx, yy): continue
                if idx == 1:
                    if wall[x][y][xx][yy] == 1: continue
                    up[(xx, yy)] = k
                    n_wind.append((xx, yy))
                else:
                    a, b = xx -dx[d], yy - dy[d]
                    if wall[x][y][a][b] == 1 or wall[a][b][xx][yy] == 1 : continue
                    up[(xx, yy)] = k
                    n_wind.append((xx, yy))
        if not n_wind: break
        wind = n_wind


    for pos, v in up.items():
        temp[pos[0]][pos[1]] += v


        
def control():
    
    up_down = defaultdict(int)
    for x in range(N):
        for y in range(M):
            for k in [1, 4]:
                xx, yy = dx[k]+x, dy[k]+y
                if not within(xx, yy): continue
                if wall[x][y][xx][yy] == 1: continue
                cha = abs(temp[xx][yy] - temp[x][y])
                cha = cha//4
                a, b = cha, cha
                if temp[xx][yy] > temp[x][y]:
                    b = -cha
                else:
                    a = -cha
                up_down[(xx, yy)] += b
                up_down[(x, y)] += a


    for k , v in up_down.items():
        if temp[k[0]][k[1]] + v < 0:
            temp[k[0]][k[1]] = 0
        else:
            temp[k[0]][k[1]] += v



        
            
            
                    
    

#main
N, M, K = map(int, input().split())
gra = [list(map(int, input().split())) for _ in range(N)]
wall = [[[[0]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
temp = [[0]*M for _ in range(N)]

#벽만들기
for _ in range(int(input())):
    x, y, t = map(int, input().split())
    x, y = x-1, y-1
    if t == 0: 
        wall[x][y][x-1][y] = 1
        wall[x-1][y][x][y] = 1
    else:
        wall[x][y][x][y+1] = 1
        wall[x][y+1][x][y] = 1
        
#온풍기, check 해야하는 칸
heater, check = [], []
for i in range(N):
    for j in range(M):
        if gra[i][j] == 0: continue
        if gra[i][j] == 5:
            check.append((i, j))
        else:
            heater.append((i, j))
def down():
    for i in range(N):
        for j in range(M):
            if i == 0 or j == 0 or i == N-1 or j == M-1:
                if temp[i][j]:
                    temp[i][j] -= 1
                    
                   
    
            
#답 도출 시작
res = 101
for r in range(1, 101):
    
    #1) 히터 켜기 
    for x, y in heater:
        d = gra[x][y]
        on(x+dx[d], y+dy[d], d)

    
    #2) 온도 조절
    control()
    
    #3) 1행, N-1행, 1열, M-1열 down
    down()
    
    for x, y in check:
        if temp[x][y] < K: break
    else:
 
        res = r
        break
    
print(res)
