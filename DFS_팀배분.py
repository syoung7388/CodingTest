def DFS(n):
    global f
    ch[n] = 1
    res[f].append(n)
    arr = not(f)
    f = arr
    for g in G[n]:
        if ch[g] == 1: continue
        DFS(g)
        f = arr
N= int(input())

G= [[] for _ in range(N+1)]
for  i in range(1, N+1):
    temp= list(map(int, input().split()))
    for j in range(temp[0]):
        G[i].append(temp[j+1])
        
ch= [0]*(N+1)
res= [[] for _ in range(2)]
f = False
for a in range(1, N+1):
    if ch[a] == 1: continue
    DFS(a)

print(len(res[0]))
print(' '.join(map(str, sorted(res[0]))))
print(len(res[1]))
print(' '.join(map(str, sorted(res[1]))))
