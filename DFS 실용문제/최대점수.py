


def DFS(id, time, sc, s):
    global bf
    if time > MT:     
        return
    if id > N:
        return
    if sc > bf:
        bf = sc
    for i in range(s, N+1):
        DFS(id+1, time+info[i-1][1],sc+info[i-1][0], i+1)
            
if __name__ == "__main__":
    N, MT = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]
    bf = -2147000000
    DFS(0, 0, 0, 1)
    print(bf)
    
