import sys
def DFS(node, cnt):
    if node == E-1:
        print(cnt)
        sys.exit(0)
    else:
        for next in G[node]:
            if ch[next] == 0:
                ch[next] = 1
                DFS(next, cnt+1) 

if __name__=="__main__":
    N = int(input()) #사람수
    S, E = map(int, input().split())
    G = [[] for _ in range(N)]
    M = int(input())
    for _ in range(M):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    ch = [0]*N
    ch[S-1] = 1
    DFS(S-1, 0)
    print(-1)
