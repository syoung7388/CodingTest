from collections import deque
import sys

N = int(input())
gra = [[1]*(N+2)]
for _ in range(N):
    a = [1]+[0]*(N)+[1]
    gra.append(a)
gra.append([1]*(N+2))

K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    gra[a][b] = 2


turn = list(map(lambda x : [int(x[0]), x[1]], [input().split() for _ in range(int(input()))] ))
turn.sort(reverse = True)


d = [0, 1, 2, 3]
dic = {0:[0,1], 1:[1,0], 2:[0,-1], 3:[-1, 0]}
now_d = 0

Q = deque([(1, 1)])
gra[1][1] = 1
time = 0

while True:

    x, y = Q[0][0], Q[0][1]
    xx, yy = dic[d[now_d]][0]+x, dic[d[now_d]][1]+y
    if gra[xx][yy] == 1:
        print(time+1)
        break
    elif gra[xx][yy] == 2:
        Q.appendleft((xx, yy))
        gra[xx][yy] = 1
        time += 1
    elif gra[xx][yy] == 0:
        Q.appendleft((xx, yy))
        gra[xx][yy] = 1
        gra[Q[-1][0]][Q[-1][1]] = 0
        Q.pop()
        time += 1
    if turn and time == turn[-1][0]:
        if turn[-1][1] == 'L':
            now_d -= 1
        else:
            now_d += 1
        if now_d == 4 or now_d == -4:
            now_d = 0
        turn.pop()

        
    
