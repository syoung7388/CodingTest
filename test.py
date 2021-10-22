N, M = map(int, input().split())
gra = [list(map(int, input())) for _ in range(N)]


for i in range(N):
    for j in range(M):
        if i == 0 and j == 0: continue
        if i == 0:
            gra[i][j] += gra[i][j-1]
        elif j == 0:
            gra[i][j] += gra[i-1][j]
        else:
            gra[i][j] += gra[i-1][j] + gra[i][j-1] - gra[i-1][j-1]



res = 0
for i in range(N-1):
    for j in range(M-1):
        a = gra[-1][j]
        b = gra[i][-1] - gra[i][j]
        c = gra[-1][-1] - a -b

        res = max(res, a*b*c)


        
        a = gra[i][j]
        b = gra[-1][j] - gra[i][j]
        c = gra[-1][-1]- gra[-1][j]

        res = max(res, a*b*c)


        
        a = gra[i][-1]
        b = gra[-1][j] - gra[i][j]
        c = gra[-1][-1] - a -b

        res = max(res, a*b*c)


        
        a = gra[i][j]
        b = gra[i][-1] - gra[i][j]
        c = gra[-1][-1] - gra[i][-1]

        res = max(res, a*b*c)



for x1 in range(N-2):
    for x2 in range(N-1):


        a, b, c = gra[x1][-1], gra[x2][-1] - gra[x1][-1], gra[-1][-1] - gra[x2][-1]
        res = max(res, a*b*c)

        
for y1 in range(M-2):
    for y2 in range(M-1):


        a, b, c = gra[-1][y1], gra[-1][y2] - gra[-1][y1], gra[-1][-1] - gra[-1][y2]
        res = max(res, a*b*c)
print(res)
        
