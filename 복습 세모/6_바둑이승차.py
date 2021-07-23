


def DFS(L, S, AS):
    global bf
    if (tot-AS) + S < bf:
        return
    if S > C:
        return

    if L == N:
        bf = max(bf, S)
        return
    

    DFS(L+1, S+kg[L], AS+kg[L])
    DFS(L+1, S, AS+kg[L])
    







if __name__ == "__main__":

    C, N = map(int, input().split())
    kg = [int(input()) for _ in range(N)]
    bf = -1
    tot = sum(kg)

    DFS(0, 0, 0)

    print(bf)
    
    
    
    
