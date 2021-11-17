from collections import deque
import sys
import heapq
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


def BFS(i, j, G, cnt):

    s_ch = [[0]*4 for _ in range(4)]
    s_ch[i%4][j%4] = 1
    Q = deque([(cnt, i%4, j%4)])

    
    temp = []
    t_ch = set()
    while Q:
        c, x, y = Q.popleft()

        if G[x][y] == 'E':
            print(c)
            sys.exit(0)
        
        
        #회전 시키고 삐쳐 나가는거 확인
        hx, hy = x, y
        for i in range(4):
            hx, hy = hy, 4-hx-1
            for k in range(4):
                xx, yy = dx[k]+hx, dy[k]+hy
                if (0<=xx<4 and 0<=yy<4): continue
                nx, ny = xx+tx*4, yy+ty*4 #전체크기로 키우기
                if 0<=nx<N and 0<=ny<N and gra[nx][ny] != '#':
                    if not (nx, ny) in t_ch:
                        t_ch.add((nx, ny))
                        temp.append((c+1+i, nx, ny)) #4격자이동 & 회전          
            

        for k in range(4):
            xx, yy = dx[k]+x, dy[k]+y
            if not (0<=xx<4 and 0<=yy<4) or gra[xx][yy] == '#': continue
            if s_ch[xx][yy] != 1:
                s_ch[xx][yy] = 1
                Q.append((c, xx, yy))
    print(temp)

    return temp
            
                    




K = int(input())
N = 4*K
gra = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

#전체 대가리들 체크용도(보류)
ch = [[0]*K for _ in range(K)]

for i in range(N):
    for j in range(N):
        if gra[i][j] == 'S':
            sx, sy = i, j
            break

         #(대가리들체크) (전체위치)
TQ = [(0, sx//4, sy//4, sx, sy)]

while TQ:
    #print(TQ)
    cnt, tx, ty, cx, cy = heapq.heappop(TQ)
    if gra[cx][cy] == 'E':
        print(cx, cy)
        print(cnt)
        sys.exit(0)
    #if ch[tx][ty] == 1: continue
    #ch[tx][ty] = 1

    G = [[0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
           # print(i, j, "->", i+(tx*4),j+(ty*4))
            G[i][j] = gra[i+(tx*4)][j+(ty*4)]

    tem = BFS(cx, cy, G, cnt)
    for rc, rx, ry in tem:
        heapq.heappush(TQ, (rc, rx//4, ry//4, rx, ry))
    
print(-1)      


