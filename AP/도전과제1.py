N = int(input())
dy = [0]*(N+1)
dy[1] = 1
dy[2] = 2

def DFS(N):
    if dy[N] >0:
        return dy[N]
    if N == 1 or N == 2:
        return dy[N]
    else:
        dy[N] = DFS(N-2)+DFS(N-1)
        return dy[N]




print(DFS(N))

print(dy)
