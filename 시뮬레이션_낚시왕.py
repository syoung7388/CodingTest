import sys
input = sys.stdin.readline

turn = [1, 0, 3, 2]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
def up_left(cur, s, L, d):
    if cur - 1 >= s:
        cur -= s
    else:
        s -= cur-1
        r = s // (L-1)
        remain = s%(L-1)
        if r%2 == 0:
            cur = 1+remain
            d = turn[d]
        else:
            cur = L - remain
    return cur,d    



def down_right(cur, s, L, d):
    if L-cur >= s:
        cur += s
    else:
        s -= L-cur
        r = s // (L-1)
        remain = s %(L-1)
        if r%2 == 0:
            cur = L - remain
            d = turn[d]
        else: 
            cur = 1+remain
    return cur,d


def move(cx, cy):
    nQ = []
    for z, x, y, s, d in sorted(Q, reverse = True):
        if x == cx and y == cy: continue #잡은 상어는 버리기
        if gra[x][y] == z:
            gra[x][y] = 0
        if d == 2:
            y,d = down_right(y, s, M, d)
        elif d == 3:
            y,d = up_left(y, s, M, d)
        elif d == 0:
            x,d = up_left(x, s, N, d)
        else:
            x,d = down_right(x, s, N, d)
        if z > gra[x][y]:
            gra[x][y] = z
            nQ.append((z, x, y, s, d))

    return nQ
        

N, M, C = map(int, input().split())
gra = [[0]*(M+1) for _ in range(N+1)]
Q = []
for _ in range(C):
    x, y, s, d, z = map(int, input().split())
    gra[x][y] = z
    Q.append((z, x, y, s, d-1)) #큰 상어가 먼저 나오도록 설정 !

cnt = 0


for j in range(1, M+1):

    #낚시왕 상어 잡기
    cx, cy = 0, 0
    for i in range(1, N+1):
        if gra[i][j] != 0:
            cnt += gra[i][j]
            gra[i][j] = 0
            cx, cy = i, j
            break

    
    #상어 이동
    Q = move(cx, cy)
    if not Q: break

            
print(cnt)
