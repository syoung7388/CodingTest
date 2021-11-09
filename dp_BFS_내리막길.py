
#dp : Memoization
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
def Move(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    
    if x == N-1 and y == M-1:
        dp[x][y] = 1
        return 1
    X = 0
    for k in range(4):
        xx, yy = dx[k]+x, dy[k]+y
        if not (0<=xx<N and 0<=yy<M):continue
        if gra[xx][yy] < gra[x][y]:
            X += Move(xx, yy)
    
    dp[x][y] = X
    return X

    
N, M = map(int, input().split())
gra = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1]*(M) for _ in range(N)]

print(Move(0, 0))




#BFS + heapq
""" 

import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
gra = [list(map(int, input().split())) for _ in range(N)]
ch = [[0]*M for _ in range(N)]
ch[0][0] = 1

Q = [(-gra[0][0], 0, 0)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
while Q:
    cnt, x, y = heapq.heappop(Q)
    for k in  range(4):
        xx, yy = dx[k]+x, dy[k]+y
        if not (0<=xx<N and 0<=yy<M) or gra[xx][yy] >= gra[x][y]: continue
        if ch[xx][yy] == 0:
            heapq.heappush(Q, (-gra[xx][yy], xx, yy))
        ch[xx][yy] += ch[x][y]


print(ch[-1][-1])
"""
