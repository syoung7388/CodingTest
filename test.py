#시뮬레이션
#시키는대로 구현하고, 방향전환하라고 할때 방향전환 해야함
#뱀길이는 Q로 구현 1111
from collections import deque
N = int(input())
gra = [[0]*(N) for _ in range(N)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    gra[a-1][b-1] = 2

turn = deque()
for _ in range(int(input())):
    a, b = map(str, input().split())
    turn.append((int(a), b))

Q = deque([(0, 0)])
gra[0][0] = 1
xy = [[0,1],[1, 0],[0,-1],[-1, 0]]
cnt = 0
d = 0
while True:
    cnt += 1
    xx, yy = xy[d][0]+Q[0][0], xy[d][1]+Q[0][1]
    
    if not(0<=xx<N and 0<=yy<N) or gra[xx][yy] == 1:
        break
    if gra[xx][yy] == 2: #사과
        Q.appendleft((xx, yy))
        gra[xx][yy] = 1
    elif gra[xx][yy] == 0: #빈칸 - 꼬리짜르기
        Q.appendleft((xx, yy))
        gra[xx][yy] = 1
        gra[Q[-1][0]][Q[-1][1]] = 0
        Q.pop()
    
    if turn and cnt == turn[0][0]:
        n, o = turn.popleft()
        if o == 'L':
            d -= 1
        elif o == 'D':
            d += 1
    if d == -4 or d == 4:
        d = 0
            
print(cnt)     
