import sys
input = sys.stdin.readline
from itertools import combinations

def Move(pos):
    global res
    for i in range(N):
        for j in range(M):
            s = 0
            for k in range(4):
                xx, yy = pos[k][0]+i, pos[k][1]+j
                if not (0<=xx<N and 0<=yy<M):
                    break
                s += gra[xx][yy]
            else:
                res = max(res, s)


def Turn(pos, a1, a2, n):

    t = [a1, a2]
    flag = False
    for _ in range(n):
        ch = [[0]*M for _ in range(N)]
        for x, y in pos:
            ch[x][y] = 1



        
        Move(pos)
        for i in range(4):
            a, b = pos[i]
            pos[i] = (b, t[flag] - a -1)
        flag = not(flag)
    

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
N, M = map(int, input().split())
gra = [list(map(int, input().split())) for _ in range(N)]

res  =0

Turn([(0,0),(0, 1), (1, 0), (2,0)], 3, 2, 4)
Turn([(0,0),(0, 1), (1, 1), (2,1)], 3, 2, 4)
Turn([(0,0),(0, 1), (0, 2), (0, 3)], 1, 4, 2)
Turn([(0, 0), (0, 1), (1, 0), (1, 1)], 0, 0, 1)
Turn([(0,0),(1, 0), (1, 1), (2,1)], 3, 0, 2)
Turn([(0,1),(2, 1), (1, 0), (2,0)], 3, 0, 2)
Turn([(0, 0), (1, 0), (2, 0), (1, 1)], 3, 2, 4)

print(res)
