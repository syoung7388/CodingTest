def getDis(a, b):
    return abs(position[a][0] - position[b][0])+abs(position[a][1]-position[b][1])


import math
N = int(input())
position = [(1,1), (N,N)]
for _ in range(int(input())):
    position.append(tuple(map(int, input().split())))
P = len(position)
position.insert(0,(0, 0))
dp = [[[math.inf, ""]for _ in range(P+1)] for _ in range(P+1)]
dp[1][2][0] = 0
for x in range(1,P):
    for y in range(1,P):
        next = max(x, y)+1
        #1번 경찰차가 가져가기
        one = dp[x][y][0]+ getDis(x,next)
        if one < dp[next][y][0]:
            dp[next][y][0] = one
            dp[next][y][1] = dp[x][y][1]+"1"
        #2번 경찰차가 가져가기
        two = dp[x][y][0]+ getDis(next, y) 
        if two < dp[x][next][0]:
            dp[x][next][0] = two
            dp[x][next][1] = dp[x][y][1]+"2"
    





res = math.inf
order = ""
for d in dp:
    if d[P][0] < res:
        res = min(res, d[P][0])
        order = d[P][1]

for r in dp[-1]:
    if r[0] < res:
        res = min(res, r[0])
        order = r[1]

