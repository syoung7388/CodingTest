from collections import deque


S, E = map(int, input().split())

Max = 100000
dis = [[-1, 0] for _ in range(Max+1)]

dis[S] = [0, 1]
Q = deque()
Q.append(S)

while Q:
    now = Q.popleft()
    if now == E:
        break
    for next in (now+1, now-1, now*2):
        if not(0<=next<=Max): continue
        if dis[next][0] == -1:
            dis[next][0] = dis[now]+1
            dis[next][1] = dis[now][1]
            Q.append(next)
        elif dis[next][0] == dis[now][0]+1:
            dis[next][1] += 1
print(dis[E][0])
print(dis[E][1])
