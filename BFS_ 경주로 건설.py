import sys
from collections import deque
def solution(board):
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] 
    N = len(board)
    dp = [[[sys.maxsize]*4 for _ in range(N)] for _ in range(N)]
    dp[0][0] = [0, 0, 0, 0]
    
    Q = deque([(0,0,-1)]) #시작점을 모두 다로 하기위해서이다능
                          #내가 틀린 부분
    
    while Q:
        x, y, d = Q.popleft()
        for k in range(4):
            xx, yy = dx[k]+x, dy[k]+y
            if not(0<=xx<N and 0<=yy<N) or board[xx][yy] == 1: continue
            cost = 100
            if k != d and d != -1:
                cost += 500 
            if dp[x][y][d]+cost < dp[xx][yy][k]:   
                Q.append((xx, yy, k))
                dp[xx][yy][k] = dp[x][y][d]+cost
    return min(dp[-1][-1])
