
from collections import deque
import sys
input = sys.stdin.readline
def bfs():
    ch = [[[0]*4 for _ in range(N)] for _ in range(M)]
    ch[sx-1][sy-1][sd-1] = 1
    Q = deque([(sx-1, sy-1, sd-1, 0)])
    
    while Q:
        x, y, d, cnt = Q.popleft()
        
        # 이새끼가 도착점에 먼저 도착했니 ?
        if (x, y, d) == (ex-1, ey-1, ed-1):
            return cnt
        
        # 새끼야 앞으로 몇칸 갈거임 ? 세칸 안으로 가능
        for k in range(1, 4):
            xx = x+ dx[d]*k
            yy = y+ dy[d]*k
            if not(0<=xx<M and 0<=yy<N) or gra[xx][yy] == 1:
                break
            if ch[xx][yy][d]==0:
                ch[xx][yy][d] = 1
                Q.append((xx, yy, d, cnt+1))
         
        # 방향도 한번 바꿔보자아 
        for dir in change[d]:
            if ch[x][y][dir] == 0:
                ch[x][y][dir] = 1
                Q.append((x, y, dir, cnt+1))
                

if __name__ == "__main__":
    dx= [0, 0, 1, -1]
    dy= [1, -1, 0, 0]
    change = [(2, 3), (2, 3), (0, 1), (0, 1)]
    
    M, N = map(int, input().split())
    gra = [list(map(int, input().split())) for _ in range(M)]
    sx, sy, sd = map(int, input().split())
    ex, ey, ed = map(int, input().split())
    
    print(bfs())
