

from collections import deque

F, S, E, U, D = map(int, input().split())


dis = [-1]*(F+1)
dis[S] = 0
Q = deque([S])

while Q:
    now = Q.popleft()
    if now == E:
        break
    for next  in (now+U, now -D):
        if not (1<= next<=F): continue
        if dis[next] == -1:
            dis[next] = dis[now]+1
            Q.append(next)
if dis[E] == -1:
    print("use the stairs")

else:
    print(dis[E])
