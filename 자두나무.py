

def Zado(a, m):
    if apple[a] == m%2+1:
        dy[a+1][m] = max(dy[a+1][m], dy[a][m] +1) #사과 받아먹기
        if m+1 > M: return
        dy[a+1][m+1] = max(dy[a][m] ,dy[a+1][m+1]) #이동후 사과 못받아 먹기  
    else:
        dy[a+1][m] = max(dy[a+1][m], dy[a][m])
        if m+1 > M: return
        dy[a+1][m+1] = max(dy[a][m]+1 ,dy[a+1][m+1])



A, M = map(int, input().split())
dy = [[-1 for _ in range(M+1)] for _ in range(A+1)]
dy[0][0] = 0 #초기값


apple = [int(input()) for _ in range(A)]
for a in range(A): #떨어지는 사과
    for m in range(M+1):#움직임 수
        if dy[a][m]!= -1:
            Zado(a, m)
                

print(max(dy[A]))
