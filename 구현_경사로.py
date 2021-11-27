import sys
input = sys.stdin.readline
def check(x, y, dx, dy):
    k = 1
    for _ in range(N-1):
        xx, yy = x+dx, y+dy
        diff = gra[xx][yy] - gra[x][y]
        if abs(diff) > 1: return 0
        if diff == 1:
            if k>=L:
                k = 0
            else:
                return 0
        if diff == -1:
            if k>=0:
                k = -L
            else:
                return 0
        k += 1
        x, y = xx, yy
    
    return 1 if k>=0 else 0

    
    
    
    
#지나갈수 있는 길의 개수
N, L = map(int, input().split())
gra = [list(map(int, input().split())) for _ in range(N)]

res = 0
for i in range(N):
    res += check(i, 0, 0, 1)
    res += check(0, i, 1, 0)
print(res)  
