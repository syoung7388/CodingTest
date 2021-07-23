



def DFS(L, sum, time):


    global bf
    if time> M:
        return
    if L == N:
        if sum > bf:
,            bf = sum
        return

    DFS(L+1, sum+sc[L], time+t[L])
    DFS(L+1, sum, time)
    


if __name__ == "__main__":
    N, M = map(int, input().split())

    sc = list()
    t = list()
    tot = sum(sc)

    for _ in range(N):
        a, b = map(int, input().split())
        sc.append(a)
        t.append(b)

    bf = -1
    DFS(0,0,0)
    print(bf)
