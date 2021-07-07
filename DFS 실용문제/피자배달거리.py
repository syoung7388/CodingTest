def DFS(L, s):
    global bf
    if L == M:
        sum = 0
        for h in range(len(ho)):
            dis = 2147000000
            x1= ho[h][0]
            y1 = ho[h][1]
            for c in ch:
                x2 = pz[c][0]
                y2 = pz[c][1]
                dis = min(abs(x1-x2)+abs(y1-y2),dis)
            sum += dis
        if sum < bf:
            bf = sum

    else:
        for i in range(s, len(pz)):
            ch[L] = i
            DFS(L+1, i+1)
 
if __name__ == "__main__":
    N, M = map(int, input().split())
    gra = [list(map(int, input().split())) for _ in range(N)]
    ch = [0]*M
    pz = []
    ho = []
    bf  = 2147000000
    for i in range(N):
        for j in range(N):
            if gra[i][j] == 2:
                pz.append((i, j))
            elif gra[i][j] == 1:
                ho.append((i,j))
    DFS(0,0)
    print(bf)
 
