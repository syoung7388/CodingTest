import sys
from collections import deque


def grouping(i, j):
    q = deque([(i, j)])
    world[i][j] = gid

    while q:
        qx, qy = q.popleft()
        for k in range(4):
            x, y = qx+dx[k], qy+dy[k]

            if 0<=x<N and 0<=y<N:
                if world[x][y] == 1:
                    world[x][y] = gid
                    q.append((x, y))
                elif world[x][y] == 0 and not (qx, qy) in ocean:
                    ocean.append((qx, qy))

def getdis():
    loop = 0
    ans = sys.maxsize
    while ocean:
        loop += 1
        length = len(ocean)
        for _ in range(length):
            ox, oy = ocean.popleft()
            for k in range(4):
                x, y = ox+dx[k], oy+dy[k]
                if 0<=x<N and 0<=y<N :
                    if world[x][y] == 0:
                        world[x][y] = world[ox][oy]
                        ocean.append((x, y))
                    elif world[x][y] < world[ox][oy]:
                        ans = min(ans, (loop-1)*2)
                    elif world[x][y] > world[ox][oy]:
                        
                        ans = min(ans, loop*2 -1)
    return ans
N = int(input())
world = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [-1,0,1,0], [0,1,0,-1]
ocean = deque()
gid = -1

for i in range(N):
    for j in range(N):
        if world[i][j] > 0:
            grouping(i, j)
            gid -= 1


print(getdis())
