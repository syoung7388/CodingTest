def DFS(now):
    ch[now] = 1    
    for next in G[now]:
        if ch[next] == 0:
            DFS(next)

if __name__ == "__main__":
    N = int(input())
    G = [[] for _ in range(N)]
    
    for _ in range(int(input())):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    ch = [0]*N
    DFS(0)
    print(G)
    print(ch.count(1)-1)
