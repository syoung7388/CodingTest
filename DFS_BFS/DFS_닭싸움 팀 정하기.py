import sys
input = sys.stdin.readline
def DFS(now):
    ch[now] = 1
    for i in F[now]:
        if ch[i] == 0:
            DFS(i)

if __name__=="__main__":
    
    N = int(input())
    E = [[] for _ in range(N+1)]
    F = [[] for _ in range(N+1)] 
    for _ in range(int(input())):
        rel , a, b = map(str, input().split())
        a, b = int(a), int(b)
        if rel == 'E':
            E[a].append(b)
            E[b].append(a)
        else:
            F[a].append(b)
            F[b].append(a)
    for e in E:
        if len(e) < 2: continue
        for i in e:
            for j in e:
                if i == j:continue
                F[i].append(j)

    ch = [0]*(N+1)
    res = 0
    for c in range(1, N+1):
        if ch[c] == 0:
            res += 1
            DFS(c)
    print(res)
    
                
