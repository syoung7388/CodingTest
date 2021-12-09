import sys
input = sys.stdin.readline
dx, dy = [-1, 0, 1,0], [0, 1, 0, -1]

def choose(f):
    
    seat = []
    for x in range(N):
        for y in range(N):
            if gra[x][y] != 0 : continue
            cnt = 0
            love = 0
            for k in range(4):
                xx, yy = dx[k]+x, dy[k]+y
                if not (0<=xx<N and 0<=yy<N): continue
                if gra[xx][yy] == 0:
                    cnt += 1
                elif like[f][gra[xx][yy]] == 1:
                    love += 1
               
            if not seat:
                seat = [love, cnt, x, y]
                continue
            
            if love > seat[0]:
                seat = [love, cnt, x, y]
            elif love == seat[0] and cnt > seat[1]:
                seat = [love, cnt, x, y]
            elif love == seat[0] and cnt == seat[1] and x < seat[2]:
                seat = [love, cnt, x, y]
            elif  love == seat[0] and cnt == seat[1] and x == seat[2] and y < seat[3]:
                seat = [love, cnt, x, y]
    return seat[2], seat[3]              



#main
N = int(input())
M = N**2
like = [[0]*(M+1) for _ in range(M+1)]
F = []
for _ in range(M):
    a, b, c, d, e = map(int, input().split())
    F.append(a)
    like[a][b],like[a][c],like[a][d], like[a][e] = 1, 1, 1, 1

gra = [[0]*N for _ in range(N)]
for f in F: 
    x, y = choose(f)
    gra[x][y] = f



res = 0    
for x in range(N):
    for y in range(N):
        cnt = 0
        for k in range(4):
            xx, yy = dx[k]+x, dy[k]+y
            if not (0<=xx<N and 0<=yy<N): continue
            if like[gra[x][y]][gra[xx][yy]] == 1:
                cnt += 1
        if not cnt : continue
        res += 10**(cnt-1)
print(res)
