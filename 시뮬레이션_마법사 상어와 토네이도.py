dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
G = [{0.05: [(0, -2)], 0.1: [(-1, -1), (1, -1)], 0.07: [(-1, 0), (1, 0)], 0.01: [(-1, 1), (1, 1)], 0.02: [(-2, 0), (2, 0)]}, {0.05: [(2, 0)], 0.1: [(1, -1), (1, 1)], 0.07: [(0, -1), (0, 1)], 0.01: [(-1, -1), (-1, 1)], 0.02: [(0, -2), (0, 2)]}, {0.05: [(0, 2)], 0.1: [(1, 1), (-1, 1)], 0.07: [(1, 0), (-1, 0)], 0.01: [(1, -1), (-1, -1)], 0.02: [(2, 0), (-2, 0)]}, {0.05: [(-2, 0)], 0.1: [(-1, 1), (-1, -1)], 0.07: [(0, 1), (0, -1)], 0.01: [(1, 1), (1, -1)], 0.02: [(0, 2), (0, -2)]}]
def expand(sx, sy, ex, ey, d):
    global res

  
    rx, ry = ex+dx[d], ey+dy[d] #나머지 들어갈곳
    
    val = gra[ex][ey] #y
    
    #비율칸에 퍼트리기
    for k, v in G[d].items():
        for a, b in v:
            e = int(gra[ex][ey]*k)
            x, y = ex+a,ey+b
            if not (0<=x<N and 0<=y<N):
                res += e
            else:
                gra[x][y] += e
            val -= e
    
    #남은거 있으면 나머지칸
    if val:
        if not (0<=rx <N and 0<=ry<N):
            res += val
        else:
            gra[rx][ry] += val
    gra[ex][ey] = 0



N = int(input())
gra = [list(map(int, input().split())) for _ in range(N)]
flag = True
d = 0
L = 1
x, y = N//2, N//2
res = 0

while flag:
    for i in range(4):
        if not flag: break
        for _ in range(L):
            xx,yy = dx[d]+x, dy[d]+y
            if gra[xx][yy]:
                expand(x, y, xx, yy, d)
            if xx == 0 and yy == 0:
                flag = False
                break
            x, y = xx, yy
            
        if i== 1: L+= 1
        d += 1
        if d == 4 : d = 0
    L+=1
print(res)
