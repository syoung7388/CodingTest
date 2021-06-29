from collections import deque

N, M = map(int, input().split())


gra = [[0]*(N+1) for _ in range(N+1)]
deg = [0]*(N+1)
dq = deque()
for m in range(M):
    w1, w2 = map(int, input().split())
    gra[w1][w2] = 1
    deg[w2] += 1

for i in range(1, N+1):
    if deg[i] == 0:
        dq.append(i)


while dq:
    x = dq.popleft()
    print(x, end=" ")
    for y in range(1, N+1):
        if gra[x][y] == 1:
            deg[y] -= 1
            if deg[y] == 0:
                dq.append(y)
                
    
    
