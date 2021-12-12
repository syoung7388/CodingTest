import sys
input = sys.stdin.readline

dx, dy = [0, 0, -1, -1, -1, 0, 1, 1, 1], [0, -1, -1, 0, 1, 1, 1, 0, -1]
hx, hy = [-1, -1, 1, 1], [-1, 1, -1, 1]


def move(d, s):
    for i in range(len(cloud)):
        x, y = cloud[i]
        xx, yy = (dx[d]*s+x)%N, (dy[d]*s+y)%N
        cloud[i] = [xx, yy]
        gra[xx][yy] += 1
        ch[xx][yy] = 1
     
def rain():
    
    for x, y in cloud:
        cnt = 0
        for k in range(4):
            xx, yy = hx[k]+x, hy[k]+y
            if not (0<=xx<N and 0<=yy<N): continue
            if gra[xx][yy] > 0:
                cnt += 1
        gra[x][y] += cnt
        
                
        
        

N, M = map(int, input().split())
gra = [list(map(int, input().split())) for _ in range(N)]

cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
for _ in range(M):
    ch = [[0]*N for _ in range(N)]
    d, s = map(int, input().split())
    
    move(d, s)
    
    rain()
    
    cloud = []
    for i in range(N):
        for j in range(N):
            if gra[i][j] >= 2 and ch[i][j] == 0:
                gra[i][j] -= 2
                cloud.append([i, j])
                
print(sum(sum(g) for g in gra))
