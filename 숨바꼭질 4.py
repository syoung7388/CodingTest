from collections import deque

if __name__ == "__main__":
    N, K = map(int, input().split())
    Max  = 100000
    dis = [0]*(Max+1)
    mov = [0]*(Max+1)
    Q =deque()
    Q.append(N)
    dis[N] = 0
    while Q:
        now = Q.popleft()
        if now == K:
            break
        for next in (now+1, now-1, now*2):
            if 0<=next<=Max and dis[next] == 0:
                dis[next] = dis[now]+1
                mov[next] = now
                Q.append(next)
    print(dis[K])
    
    res = list()
    idx = K
    for _ in range(dis[K]+1):
        res.append(idx)
        idx = mov[idx]

    print(' '.join(map(str, res[::-1])))
