

import sys
input = sys.stdin.readline
from collections import deque
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


def BFS(i, j):
    Q = deque([(i, j)])
    ch[i][j] = 1
    s = gra[i][j]
    n_tq = set()
    arr = [(i, j)]
    while Q:
        x, y = Q.popleft()
        for k in range(4):
            xx, yy = dx[k]+x, dy[k]+y
            if not (0<=xx<N and 0<=yy<N) or ch[xx][yy] == 1: continue
            if L <= abs(gra[xx][yy] - gra[x][y]) <= R:
                Q.append((xx, yy))
                s += gra[xx][yy]
                ch[xx][yy] = 1
                arr.append((xx, yy))
            else:
                n_tq.add((x, y))


    for nx, ny in n_tq:
        TQ.append((nx, ny))

    if len(arr) > 1:
        p_num = s//len(arr)
        for ax, ay in arr:
            gra[ax][ay] = p_num
        return True
    return False
                

    


    
N, L, R = map(int, input().split())
gra = [list(map(int, input().split())) for _ in range(N)]


TQ = deque()
for i in range(N):
    for j in range(N):
        TQ.append((i, j))


res = 0
while True:

    ch = [[0]*N for _ in range(N)]
    f = False
    for _ in range(len(TQ)):

        i, j = TQ.popleft()
        if ch[i][j] == 1: continue
        if BFS(i, j):
            f = True
    if f:
        res += 1
    else:
        break
print(res)
