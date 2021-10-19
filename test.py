def DFS(n):
    if n == N:
        res.append(P)
        return
    for i in range(N):
        if ch[i] != 0: continue    
        a = P.index(-1)
        b = a + arr[i] + 1
        if b >= N*2 or P[b] != -1: continue
        P[a] = arr[i]
        P[b] = arr[i]
        ch[i] = 1
        DFS(n+1)
        P[a] = -1
        P[b] = -1
        ch[i] = 0


#숌사이의 수열 
N = int(input())
arr = list(map(int, input().split()))
ch = [0]*(N+1)
P = [-1]*(N*2)
res = []
DFS(0)
res.sort()
if res:
    for r in res[0]:
        print(r, end = " ")
        
else:
    print(-1)
