
def DFS(now):
    global flag
    if now == N+1:
        flag =  True
    
    for next in G[now]:
        DFS(next)
    return 
    


for _ in range(int(input())):
    N = int(input())
    pos = [tuple(map(int, input().split())) for _ in range(N+2)]
    G = [[] for _ in range(N+2)]
    
    
    for i in range(N+2):
        for j in range(i+1, N+2):
            if abs(pos[i][0]-pos[j][0]) + abs(pos[i][1]-pos[j][1]) <= 1000:
                G[i].append(j)

    flag = False
    DFS(0)
    if flag:
        print("happy")
    else:
        print("sad")
