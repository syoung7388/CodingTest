import sys
input = sys.stdin.readline
def grouping(x, y, d1, d2):

    global res

    #1) 경계구역 구해주기 O(82)

    a, b = x+d1-1, y
    one = gra[a][b]
    for i in range(d1):
        nx, ny = x+i*1, y+i*-1
        if not (0<=nx<N and 0<=ny<N): continue
        one -= yul[a][ny] - yul[nx-1][ny]


    #제 2구역
    a, b = x+d2, N-1
    two = gra[a][b] - gra[a][y]
    for i in range(1, d2+1):
        nx, ny = x+i*1, y+i*1
        if not (0<=nx<N and 0<=ny<N): continue
        two -= yul[a][ny] - yul[nx-1][ny]


    print(x, y, d1, d2)
    #제 3구역
    a, b = N-1, y -d1+d2 -1
    tree = gra[a][b] - gra[x+d1-1][b]
    print(tree)
    for i in range(d1):
        nx, ny = (x+d1)+i*1, (y-d1)+i*1
        if not (0<=nx<N and 0<=ny<N): continue
        tree -= yul[nx][ny] - yul[x+d1-1][ny]
        
    #제 4구역
    a, b = N-1, N-1
    four = gra[a][b]- gra[a][y - d1+d2-1] - gra[x+d2][b] + gra[x+d2][y - d1+d2-1]
    for i in range(1, d2+1):
        nx, ny = (x+d2)+i*1, (y+d2)+i*-1
        if not (0<=nx<N and 0<=ny<N): continue
        four -= yul[nx][ny] - yul[x+d2][ny]



    temp = [one, two, tree, four]
    temp.append(gra[-1][-1] - sum(temp))
    temp.sort()
    res = min(temp[-1] - temp[0], res)




    
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr = list(map(list, zip(*arr)))


gra = [a[:] for a in arr]
yul = [a[:] for a in arr]
for  i in range(N):
    for j in range(N):
        if i == 0 and j == 0: continue
        if i == 0:
            gra[i][j] += gra[i][j-1]
        elif j == 0:
            gra[i][j] += gra[i-1][j]
        else:
            gra[i][j] += gra[i][j-1] + gra[i-1][j] - gra[i-1][j-1]

        if i == 0: continue 
        yul[i][j] += yul[i-1][j]

for g in gra:
    print(g)
print()
for y in yul:
    print(y)
print()


#가장 인구가 많은 선거 - 적은 선거 최솟값

res = 2147000000

for d1 in range(1, N):
    for d2 in range(1, N):
        for x in range((N-1) - (d1+d2)):
            for y in range(d1, (N-1)-d2):
                #print(x, y, d1, d2)
                grouping(x, y, d1, d2)
print(res)
