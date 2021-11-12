from collections import deque
import sys
input = sys.stdin.readline
#시간 복잡도 ?
#O(256NM) -> bit연산자 값 * N * M



dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

N, M = map(int, input().split())
gra = [list(map(str, input())) for _ in range(N)]


for  i in range(N): 
    for j in range(M):
        if gra[i][j] == '0':
            sx, sy = i, j
            break
        
Q = deque([(sx, sy, 1<<7)])

gra[sx][sy] = '.'
dis = [[[-1]*(1<<7+1) for _ in range(M)] for _ in range(N)]
dis[sx][sy][1<<7] = 0


while Q :
    x, y, key= Q.popleft()
   
    for k in range(4):
        xx, yy = dx[k]+x, dy[k]+y
        if not (0<=xx<N and 0<=yy<M): continue
        if dis[xx][yy][key] != -1: continue
        
        n = ord(gra[xx][yy])
        if 65<=n<=70 and key & (1<<(n-65)) != 0:
            Q.append((xx, yy, key))
            dis[xx][yy][key] = dis[x][y][key]+1
        elif 97<=n<=102:
            n_key = key|(1<<(n-97))
            Q.append((xx, yy, n_key))
            dis[xx][yy][n_key] = dis[x][y][key]+1
        elif n == 46:
            Q.append((xx, yy, key))
            dis[xx][yy][key] = dis[x][y][key] + 1
        elif n == 49:
            print(dis[x][y][key]+1)
            sys.exit(0)
            
        
print(-1)
