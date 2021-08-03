from collections import deque
import sys


Q = deque()
N, K = map(int, input().split())
Max= 100000
ch = [0]*(Max+1)
dis = [0]*(Max+1)
Q.append(N)
dis[N]=0
ch[N] = 1
while Q:
    now = Q.popleft()
    if now == K:
        break
    if now*2 <= Max  and ch[now*2] == 0:
        ch[now*2] = 1
        dis[now*2] = dis[now]
        Q.appendleft(now*2)
    if 0<=now-1 and ch[now-1] == 0:
        ch[now-1]= 1
        dis[now-1] = dis[now]+1
        Q.append(now-1)
    if now+1 <= Max and ch[now+1] == 0:
        ch[now+1]= 1
        dis[now+1] = dis[now]+1
        Q.append(now+1)
print(dis[K])
