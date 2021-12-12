import sys
input  = sys.stdin.readline
from collections import defaultdict
pass_dir = [[], [3, 4], [3, 4], [1, 2], [1, 2]]
dx, dy = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]

def within(x, y):
    if 0<=x<N and 0<=y<M: return True
    return False

def new_wind(d):
    a, b = pass_dir[d]
    return [[a, d], [d], [b, d]]
    
    
    
def on(i, j, d):

    wind = [(i, j)]
    up[(i, j)]+=5
    ch = [[0]*M for _ in range(N)]
    for n in range(4, 0, -1):
        n_wind = []
        for x, y in wind:
            for directs in new_wind(d):
                cx, cy = x, y
                for k in directs:
                    nx, ny = cx+dx[k], cy+dy[k]
                    if not within(nx, ny) or wall[cx][cy][nx][ny] == 1: break
                    cx, cy = nx, ny
                else:
                    if ch[cx][cy] == 1: continue
                    ch[cx][cy] = 1
                    up[(cx, cy)] += n
                    n_wind.append((cx, cy))
        if not n_wind: break            
        wind= n_wind
        
        
def control():
    
    up_down = defaultdict(int)
    
    for x in range(N):
        for y in range(M):
            for k in [1, 4]:
                xx, yy = dx[k]+x, dy[k]+y
                if not within(xx, yy) or wall[x][y][xx][yy] == 1: continue
                cha = abs(temp[xx][yy] - temp[x][y])
                cha = cha//4
                if cha == 0 : continue
                a, b = cha, cha
                if temp[x][y] > temp[xx][yy]:
                    a = -cha
                else:
                    b = -cha
                up_down[(x, y)] += a
                up_down[(xx, yy)]+= b
                
    for k, v in up_down.items():
        if temp[k[0]][k[1]]+v < 0:
            temp[k[0]][k[1]] = 0
        else:
            temp[k[0]][k[1]] += v
                

#main
N, M, K = map(int, input().split())
gra = [list(map(int, input().split())) for _ in range(N)]

#히터랑, 조사할칸 배열로 만들기, 벽도 만들기
heater = []
check = []
for i in range(N):
    for j in range(M):
        if 1<= gra[i][j] <= 4:
            heater.append((i, j))
        elif gra[i][j] == 5:
            check.append((i, j))
wall = [[[[0]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
for _ in range(int(input())):
    x, y, t = map(int, input().split())
    x, y = x-1, y-1
    if t ==0:
        wall[x][y][x-1][y] = 1
        wall[x-1][y][x][y] = 1
    elif t == 1:
        wall[x][y][x][y+1] = 1
        wall[x][y+1][x][y] = 1


res = 101
temp = [[0]*M for _ in range(N)]

up = defaultdict(int)
for x, y in heater:
    a, b = x+dx[gra[x][y]], y+dy[gra[x][y]]
    if not within(a, b): continue
    on(a, b, gra[x][y])
up = up.items()

#정답 도출 시작
for r in range(1, 101):
    
    #히터 켜기
    for k, v in up:
        temp[k[0]][k[1]] += v

    #온도 조절
    control()
    
    #1행 , 1열 , N-1행, M-1열 온도 한칸 내리기
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0: continue
            if i == 0 or i == N-1 or j == 0 or j == M-1:
                temp[i][j] -= 1
                
    #온도 >= K ?
    for cx, cy in check:
        if temp[cx][cy] < K: break
    else:
        res = r
        break
print(res)
