def make_dis():
    for i in range(N+2):
        for j in range(N+2):
            if i == j: continue
            if abs(pos[i][0]-pos[j][0])+abs(pos[i][1]-pos[j][1])<= 1000:
                G[i].append(j)
                
def DFS(node):
    ch[node] = 1
    for next in G[node]:
        if ch[next] == 0:
            DFS(next)
if __name__ == "__main__":

    for _ in range(int(input())):
        N = int(input())
        pos = [list(map(int, input().split())) for _ in range(N+2)]
        G = [[] for _ in range(N+2)]
        ch = [0]*(N+2)
        make_dis()
        DFS(0)
        
        print("happy" if ch[-1] else "sad")
