
def DFS(L, d): #카운트, S => 들어가야 하는 자릿수
    #print(L, P)
    
    if L == N or d == -2:
        res.append(P[:])
        return

    for i in range(N):
        if ch[X[i]] == 0: continue #이미 선택된 숫자

        nt = d + X[i] + 1
        
        if nt >= N*2 or P[nt] != -1 or P[d] != -1: continue

        P[nt] = X[i]
        P[d] = X[i]
        ch[X[i]] -= 1
        if -1 not in P:
            a = -2
        else:
            a = P.index(-1)   
        DFS(L+1, a)
        ch[X[i]] += 1
        P[nt] = -1
        P[d] = -1




N = int(input())
X = list(map(int, input().split()))
P = [-1]*(N*2)
ch = [0]*(max(X) + 1)
for x in X:
    ch[x] = 1
res = []
DFS(0, 0)
if res:
    res.sort()
    for r in res[0]:
        print(r, end = " ")
else:
    print(-1)
