#N수빈 K동생점 
#+1/-1:1초 *2: 1초 #가장 빠른 시간, 어떻게 이동



from collections import deque
if __name__ == "__main__":
    N, K = map(int, input().split())
    Max = 100000
    ch = [0]*(Max+1)
    dis = [0]*(Max+1)
    ch[N] = 1
    List = [[]]*(Max+1)
    List[N] += [N]
    Q = deque()
    Q.append(N)

    while Q:
        now = Q.popleft()
        if now == K:
            break
        for next in (now+1, now-1, now*2):
            if 0<= next<Max and ch[next] == 0:
                ch[next] = 1
                dis[next]= dis[now]+1
                l = List[now]
               
                List[next] += List[now]
                
                Q.append(next)
    print(dis[K][0])
    for d in dis[K][1]:
        print(d, end=" ")

