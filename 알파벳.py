import sys
input = sys.stdin.readline

def DFS(x, y, cnt):
    global res
    res = max(cnt, res)
    for k in range(4):
        xx, yy = dx[k]+x, dy[k]+y
        if not (0<=xx<R and 0<=yy<C):continue
        if P[gra[xx][yy]] == 0:
            P[gra[xx][yy]] = 1
            DFS(xx, yy, cnt+1)
            P[gra[xx][yy]] = 0
       

        
if __name__ == "__main__":
    R, C = map(int, input().split())
    gra = [list(map(lambda x: ord(x)-65, input())) for _ in range(R)]
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    P = [0]*(26)
    P[gra[0][0]] =1
    res = 0
    DFS(0,0, 1)
    print(res)
    
