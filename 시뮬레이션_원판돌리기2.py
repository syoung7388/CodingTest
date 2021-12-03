import sys
input = sys.stdin.readline

def Turn(i, d, k):
    if d == 0:
        for _ in range(k):
            gra[i] = [gra[i][-1]] + gra[i][:-1]
    else:
        for _ in range(k):
            gra[i] = gra[i][1:]+ [gra[i][0]]
def Same(ng):
    global flag
    for i in range(1, N+1):
        for j in range(M):
            if gra[i][j] == 0: continue
            if gra[i][j] == gra[i][j-1]:
                flag = False
                ng[i][j] = 0
                ng[i][j-1] = 0
            
            if i >= N: continue
            if gra[i+1][j] == gra[i][j]:
                flag = False
                ng[i][j] = 0
                ng[i+1][j] = 0
    return ng
def Change():
    s = 0
    cnt = 0
    for i in range(1, N+1):
        for j in range(M):
            if gra[i][j] == 0: continue
            s += gra[i][j]
            cnt += 1
    
    if s == 0: return
    
    t = s / cnt
    for i in range(1, N+1):
        for j in range(M):
            if gra[i][j] == 0: continue
            if gra[i][j] > t:
                gra[i][j] -= 1
            elif gra[i][j] < t:
                gra[i][j] += 1
                
                
                
    
                
N, M, T = map(int, input().split())
gra = [[0]*M]
for _ in range(N):
    gra.append(list(map(int, input().split())))

for _ in range(T):
    x, d, k = map(int, input().split())
    
    for i in range(x, N+1, x):
        Turn(i, d, k)


    flag = True
    gra = Same([g[:] for g in gra])
    
    if flag:
        Change()
res = 0
for i in range(1, N+1):
    for j in range(M):
        res += gra[i][j]
print(res)
    
