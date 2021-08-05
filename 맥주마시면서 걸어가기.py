def make_gra():
    for i in range(N+2):
        for j in range(N+2):
            if i == j:
                continue
            if abs(pos[i][0] - pos[j][0])+ abs(pos[i][1]-pos[j][1])<=1000:
                G[i].append(j)
           
           

def DFS(node):
    ch[node] = 1
    for n in G[node]:
        if ch[n] == 0:
            DFS(n)
for _ in range(int(input())):
    N = int(input()) #편의점 개수, N+2 총개수
    pos = [list(map(int, input().split())) for _ in range(N+2)]
    G = [[] for _ in range(N+2)]    
    make_gra()
    ch = [0]*(N+2)
    DFS(0)
    
    print("happy" if ch[-1] else "sad")
