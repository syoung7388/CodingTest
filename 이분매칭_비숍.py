N = int(input())
gra = [list(map(int, input().split())) for _ in range(N)]

left = [[0 for _ in range(N)] for _ in range(N)]
right = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if gra[i][j] == 1:
            right[i][j] = i+j+1

for i in range(N):
    for j in range(N):
        if gra[i][j] == 1:
            left[i][j] = i-j+N
    
link = [[] for _ in range(N*2)]

for i in range(N):
    for j in range(N):
        if gra[i][j]==1:
            link[left[i][j]].append(right[i][j])




def DFS(now):
    ch[now] = 1
    for nt in link[now]:
        if lt[nt] == 0:
            lt[nt] = now
            return True
        elif (not ch[lt[nt]] and DFS(lt[nt])):
            lt[nt] = now
            return True
    return False

lt = [0]*(2*N)
rt= [0]*(2*N)
res = 0
for i in range(1, 2*N):
    ch = [0]*(2*N)
    if DFS(i):
        res += 1

print(res)


