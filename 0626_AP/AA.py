N = int(input())
e = [list(map(int, input().split())) for _ in range(N)]
dy = [[0]*(N) for _ in range(N)]

dy[0][0] = e[0][0]

def SetNum(n1, n2):
    if dy[n1][n2] != 0:
        return dy[n1][n2]
    elif n1 == 0:
        dy[n1][n2] = SetNum(n1,n2-1)+e[n1][n2]
        return dy[n1][n2]
    elif n2 == 0:
        dy[n1][n2] = SetNum(n1-1, n2) + e[n1][n2]
        return dy[n1][n2]
    else:
        dy[n1][n2] = min(SetNum(n1-1, n2), SetNum(n1, n2-1))+ e[n1][n2]
        return dy[n1][n2]
    
print(SetNum(N-1, N-1))
