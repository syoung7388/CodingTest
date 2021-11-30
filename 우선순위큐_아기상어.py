import sys
input = sys.stdin.readline
import heapq

dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
N = int(input())
gra = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if gra[i][j] == 9:
            cx, cy = i, j
            break
            
size = 2
eat = 0
sec = 0
while True:
    H = [(sec, cx, cy)]
    F = ()
    ch = [[0]*N for _ in range(N)]
    ch[cx][cy] = 1
    gra[cx][cy] = 0
    while H:
        s, x, y = heapq.heappop(H)
        if  gra[x][y] != 0  and gra[x][y] < size:
            F = (x, y, s)
            break
        
        for k in range(4):
            xx, yy = dx[k]+x, dy[k]+y
            if not (0<=xx<N and 0<=yy<N) or ch[xx][yy] == 1: continue
            if gra[xx][yy] <= size:
                ch[xx][yy] = 1
                heapq.heappush(H, (s+1, xx, yy))
         
    if not F: break
    eat += 1
    if eat == size:
        size += 1
        eat = 0
    cx, cy, sec = F
print(sec)
