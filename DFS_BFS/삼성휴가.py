



def DFS(L, sum):
    global bf
    if L == n+1:
        if sum > bf:
            bf  = sum
        return
    else:
        for i in range(1, n+1):
            if L+T[L] <= n+1:
                DFS(L+T[L], sum+P[L])
            DFS(L+1, sum)


if __name__ == "__main__":
    n = int(input())
    T= list()
    P = list()
    for i in range(n):
        a, b = map(int, input().split())
        T.append(a)
        P.append(b)
    T.insert(0, 0)
    P.insert(0, 0)
    bf = -2147000000
    DFS(1,0)
    print(bf)
