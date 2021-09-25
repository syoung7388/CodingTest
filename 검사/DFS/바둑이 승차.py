#바둑이

import sys

def DFS(L, add, t_add):
    global bf
    if add+(total-t_add) < bf:
        return
    if add > C:
        return
    elif L == N:
        bf = max(bf, add)
    else:
        DFS(L+1, add+we[L], t_add + we[L] )
        DFS(L+1, add, t_add + we[L])

if __name__ == "__main__":
    C, N = map(int, input().split())
    we = [int(input()) for _ in range(N)]
    total= sum(we)
    bf = -2147000000
    DFS(0,0, 0)
    print(bf)
    
    
