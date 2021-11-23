import sys
input = sys.stdin.readline
def move(c):
    if c == 1: #동쪽 이일호
        return [Z[2], Z[1], Z[5], Z[0], Z[4], Z[3]]
    elif c == 2: #서쪽 차밀령
        return [Z[3], Z[1], Z[0], Z[5], Z[4], Z[2]]
    elif c == 3: #북쪽 김정일오이
        return [Z[1], Z[5], Z[2], Z[3], Z[0], Z[4]]
    elif c == 4: #남쪽 사형임
        return [Z[4], Z[0], Z[2], Z[3], Z[5], Z[1]]
N, M, x, y, K = map(int, input().split())
gra = [list(map(int, input().split())) for _ in range(N)]
cmd = list(map(int, input().split()))
Z = [0, 0, 0, 0, 0, 0]
dx, dy = [0, 0, 0, -1, 1],  [0, 1, -1, 0, 0]
for c in cmd:
    xx, yy = dx[c]+x, dy[c]+y
    if not (0<=xx<N and 0<=yy<M): continue
    Z = move(c)
    if gra[xx][yy] == 0:
        gra[xx][yy] = Z[-1]
    else:
        Z[-1] = gra[xx][yy] 
        gra[xx][yy] = 0
    x, y = xx, yy
    print(Z[0])
