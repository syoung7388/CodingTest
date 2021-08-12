import heapq
from collections import deque
def bfs(sdot):
    global bf
    ch = str(sdot)
    Q = deque()
    Q.append((0, sdot, ch))
    while Q:
        for _ in range(len(Q)):
            money, now, c = Q.popleft()
            if money > bf: continue
            if len(c)  == N:
                if gra[now][sdot] != 0:
                    bf = min(money+gra[now][sdot], bf)
                    return
                continue
            for i in range(N):
                if gra[now][i] != 0 and str(i) not in c:
                    Q.append((money+gra[now][i], i, c+str(i)))
    

if __name__ == "__main__":
    N = int(input())
    gra = [list(map(int, input().split())) for _ in range(N)]
    bf = 2147000000
    for i in range(N):
        bfs(i)
    if bf == 2147000000:
        print(0)
    else:
        print(bf)
