
import sys
sys.setrecursionlimit(10**6)

def DFS(S, L):
    print(L, P)
    if S  == N:
        res.append(''.join(map(str, P)))
        return
    for i in X:
        if ch[i] == 0: continue
        nt = L+i+1
        if nt >= N*2 or P[nt] != -1 or P[L] != -1: continue
        ch[i] -= 1
        P[nt] = i
        P[L] = i
        if not -1 in P:
            DFS(L+1, 0)
        else:
            DFS(L+1, P.index(-1))
        P[nt] = -1
        ch[i] += 1
        P[L] = -1

N = int(input())
X = list(map(int, input().split()))
P = [-1]*(N*2)
ch = [0]*(max(X) + 1)
for x in X:
    ch[x] = 1
    
res = []
DFS(0, 0)
if len(res) != 0:
    res.sort()
    for r in res[0]:
        print(r, end = " ")
else:
    print(-1)


