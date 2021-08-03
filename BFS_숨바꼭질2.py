from collections import deque
import sys


Q = deque()
N, K = map(int, input().split())
Max= 100000
Q.append(N)
ch = [0]*(Max+1)
dis = [0]*(Max+1)
ch[N] = 1
while Q:
    now = Q.popleft()
    if now == K:
        break
    for idx, next in ((0,now+1), (1, now-1), (2, now*2)):
        if 0<next<=Max:
            if ch[next] == 0:
                ch[next] =1
                if idx == 2:
                    dis[next] = dis[now]
                else:
                    dis[next] = dis[now]+1
                Q.append(next)
print(dis[K])
