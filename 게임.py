import sys
input = sys.stdin.readline
import heapq

def Grouping(x1, y1, x2, y2, n):
    sx1, sx2, sy1, sy2 = min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)

    for i  in range(sx1, sx2+1):
        for j in range(sy1, sy2+1):
            gra[i][j] = n


gra = [[0]*501 for _ in range(501)]

for _ in range(int(input())):
    x1, y1, x2, y2  = map(int, input().split())
    Grouping(x1, y1, x2, y2, 1)



for _ in range(int(input())):
    x1, y1, x2, y2  = map(int, input().split())
    Grouping(x1, y1, x2, y2, 2)


H = [(0, 0, 0)]
gra[0][0]= -1
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
res = -1
while H:
    cnt, x, y = heapq.heappop(H)
    if x == 500 and y == 500:
        res =cnt
        break

    for k in range(4):
        xx, yy = dx[k]+x, dy[k]+y
        if not (0<=xx<=500 and 0<=yy<=500) or gra[xx][yy] == -1: continue
        if gra[xx][yy] == 1:
            heapq.heappush(H, (cnt+1, xx, yy))
            gra[xx][yy] = -1
        elif gra[xx][yy] == 0:
            heapq.heappush(H, (cnt, xx, yy))
            gra[xx][yy] = -1            

print(res)    

