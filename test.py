
"""        
        (-1, 0)
           3
(0, -1)2<-(0,0)->0(0, 1) 
           1
         (1, 0)
         
"""
from collections import deque
N = int(input())

gra = [[1]*(N+2)]
for _ in range(N):
    gra.append([1]+[0]*(N)+[1])
gra.append([1]*(N+2))

Q = deque([(1, 1)])
gra[1][1] = 1
d = [(0,1), (1,0), (0,-1), (-1, 0)]

for _ in range(int(input())):
    a, b = map(int, input().split())
    gra[a][b] = 2

change = [list(map(str, input().split())) for _ in range(int(input()))]
time = 0
cur = 0
while True:
    time += 1
    x, y = Q[0][0], Q[0][1]
    xx, yy = x + d[cur][0] , y + d[cur][1]
    if gra[xx][yy] == 1:
        break
    if gra[xx][yy] == 2:
        Q.appendleft((xx, yy))
        gra[xx][yy] = 1
    elif gra[xx][yy] == 0:
        Q.appendleft((xx, yy))
        gra[xx][yy] = 1
        gra[Q[-1][0]][Q[-1][1]] = 0
        Q.pop()
    
    if time == int(change[0][0]):
        if change[0][1] == 'D':
            cur += 1
        elif change[0][1] == 'L':
            cur -= 1
        if cur == 4 or cur == -4:
            cur = 0
        change.pop(0)
            
    
print(time)
