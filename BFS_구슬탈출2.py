import sys
import heapq

def Move(x, y, a, b):
    cn = 0
    while gra[x+a][y+b] != '#' and gra[x][y] != 'O':
        x += a
        y += b
        cn += 1
    return x, y, cn

def BFS(H):
    while H:
        cnt, R, B = heapq.heappop(H)
        if cnt > 10:
            return -1
        for k in range(4):
            rx, ry, rc = Move(R[0], R[1], dx[k], dy[k])
            bx, by, bc = Move(B[0], B[1], dx[k], dy[k])
            
            if gra[rx][ry] == 'O' and gra[bx][by] != 'O':
                return cnt
            if gra[rx][ry] == 'O' or gra[bx][by] == 'O': continue
            if rx == bx and ry == by:
                if rc > bc:
                    rx -= dx[k]
                    ry -= dy[k]
                else:
                    bx -= dx[k]
                    by -= dy[k]   
            if  ch[rx][ry][bx][by] == 0:
                ch[rx][ry][bx][by] = 1
                heapq.heappush(H, (cnt + 1, (rx, ry), (bx, by)))    
    return -1
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

N, M= map(int, input().split())
gra = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if gra[i][j] == 'B':
            bx, by = i, j
        if gra[i][j] == 'R':
            rx, ry = i, j

H = [(1, (rx, ry), (bx, by))]
ch = [[[[0]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
ch[rx][ry][bx][by] = 1
print(BFS(H))
