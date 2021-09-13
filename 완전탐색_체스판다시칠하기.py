        

#주석이 나의답 시간, 메모리 비슷함, 하지만 다른사람 생각하면 처음이 더 ㄱㅊ

N,M =  map(int,input().split())
gra = [list(map(str, input())) for _ in range(N)]


res = 2147000000
for x in range(N-7):
    for y in range(M-7):
        res1 = 0 #W
        res2 = 0 #B
        for i in range(x, x+8):
            for j in range(y, y+8):
                if (i+j)%2 == 0:
                    if gra[i][j] == 'B':
                        res1 += 1
                    else:
                        res2 += 1
                else:
                    if gra[i][j] == 'W':
                        res1 += 1
                    else:
                        res2 += 1
        res = min(res,res1,res2)
print(res)
"""        
def Change(r, c):
    wcnt =0
    bcnt = 0
    for i in range(8):
        for j in range(8):
            if gra[r+i][c+j] != W[i][j]:
                wcnt+=1
            if gra[r+i][c+j] != B[i][j]:
                bcnt += 1
    return min(wcnt, bcnt)
                
N,M =  map(int,input().split())
gra = [list(map(str, input())) for _ in range(N)]
dx,dy = [-1,0,1,0],[0,1,0,-1]

W = [
    ['W','B', 'W','B','W', 'B', 'W','B'],
    ['B', 'W', 'B', 'W', 'B', 'W','B', 'W'],
    ['W','B', 'W','B','W', 'B', 'W','B'],
    ['B', 'W', 'B', 'W', 'B', 'W','B', 'W'],
    ['W','B', 'W','B','W', 'B', 'W','B'],
    ['B', 'W', 'B', 'W', 'B', 'W','B', 'W'],
    ['W','B', 'W','B','W', 'B', 'W','B'],
    ['B', 'W', 'B', 'W', 'B', 'W','B', 'W'],
     ]
B = [
    ['B', 'W', 'B', 'W', 'B', 'W','B', 'W'],
    ['W','B', 'W','B','W', 'B', 'W','B'],
    ['B', 'W', 'B', 'W', 'B', 'W','B', 'W'],
    ['W','B', 'W','B','W', 'B', 'W','B'],
    ['B', 'W', 'B', 'W', 'B', 'W','B', 'W'],
    ['W','B', 'W','B','W', 'B', 'W','B'],
    ['B', 'W', 'B', 'W', 'B', 'W','B', 'W'],
    ['W','B', 'W','B','W', 'B', 'W','B'],
    ]
res = 2147000000
for i in range(N-8+1):
    for j in range(M-8+1):
        res = min(res,  Change(i,j))
print(res)
"""
