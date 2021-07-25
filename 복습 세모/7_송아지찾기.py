#송아지 찾기


from collections import deque


S, E = map(int, input().split())
Q = deque()
Q.append(S)
Max = 10000
dis = [0]*Max
dis[S] = 1




while Q:
    now  = Q.popleft()
    if now == E:
        break
    for n in (now-1, now+1, now+5):
        if 0 <= n <Max and dis[n] == 0:
            dis[n] = dis[now]+1
            Q.append(n)
print(dis[E]-1)
