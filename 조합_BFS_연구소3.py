import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque
dx, dy  = [-1, 0, 1, 0], [0, 1, 0, -1]


def expand(com):
    global sec

    Q = deque(com)
    ch = [[-1]*N for _ in range(N)] #확산될때 초 들어가는곳
    for c in com:
        ch[c[0]][c[1]] = 0
        
     
    while Q:
        x, y = Q.popleft()
        for k in range(4):
            xx, yy = dx[k]+x, dy[k]+y
            if not (0<=xx<N and 0<=yy<N) or gra[xx][yy] == 1 : continue
            if ch[xx][yy] == -1:
                ch[xx][yy] = ch[x][y] + 1
                if gra[xx][yy] != 2 and ch[xx][yy] >= sec: return #주의 
                Q.append((xx, yy))


    s = 0
    for i in range(N):
        for j in range(N):
            if gra[i][j] == 1 or gra[i][j] == 2: continue
            if ch[i][j] == -1: return
            s = max(s, ch[i][j])
               
    sec = min(sec, s)

N, M = map(int, input().split())
gra = []
virus = []
for i in range(N):
    a = list(map(int, input().split()))
    for j in range(N):
        if a[j] == 2:
            virus.append((i, j))
    gra.append(a)


sec = 2147000000
for com in combinations(virus, M): #3개 뽑기
    expand(com)
if sec == 2147000000:
    print(-1)
else:
    print(sec)
