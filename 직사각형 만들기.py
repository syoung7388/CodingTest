import sys




N, M = map(int, input().split())
gra = [list(map(int, input())) for _ in range(N)]


res = 0

#가로로 세동가리
if N > 1:
    for x1 in range(N-1):
        for x2 in range(x1+1, N-1):
            s1, s2, s3 = 0, 0, 0
            for i in range(N):
                if i <= x1:
                    s1 += sum(gra[i])
                elif i <= x2:
                    s2 += sum(gra[i])
                else:
                    s3 += sum(gra[i])
            res = max(res, s1*s2*s3)


#세로로 세동가리


if M > 1:
    for y1 in range(M-1):
        for y2 in range(y1+1, M-1):
            s1, s2, s3 = 0, 0, 0
            for i in range(N):
                for j in range(M):
                    if j <= y1:
                        s1 += gra[i][j]
                    elif j <= y2:
                        s2 += gra[i][j]
                    else:
                        s3 += gra[i][j]
            res = max(res, s1*s2*s3)







if N == 1 :
    for i in range(1, M):
        gra[0][i] +=  gra[0][i-1]
    for x1 in range(M-1):
        for x2 in range(x1+1, M-1):
            res = max(res, gra[0][x1]*(gra[0][x2] - gra[0][x1])*(gra[0][M-1] - gra[0][x2]))
    print(res)
    sys.exit(0)
    
if M == 1 :
    for i in range(1, N):
        gra[i][0] +=  gra[i-1][0]
    for x1 in range(N-1):
        for x2 in range(x1+1, N-1):
            res = max(res, gra[x1][0]*(gra[x2][0] - gra[x1][0])*(gra[N-1][0] - gra[x2][0]))
    print(res)
    sys.exit(0)            



for x in range(N-1): #X축 기준점
    for y in range(M-1): #Y축 기준점
        s1, s2, s3 = 0, 0, 0
        a1, a2, a3 = 0, 0, 0
        
        u1, u2, u3 = 0, 0, 0
        d1, d2, d3 = 0, 0, 0
        for i in range(N):
            for j in range(M):
                if i <= x and j <= y:
                    s1 += gra[i][j]
                elif i > x and j <= y:
                    s2 += gra[i][j]
                else:
                    s3 += gra[i][j]

                if j <= y:
                    a1 += gra[i][j]
                elif i <= x and j > y:
                    a2 += gra[i][j]
                else:
                    a3 += gra[i][j]


                if i <= x and j <= y:
                    u1 += gra[i][j]
                elif i <= x and j > y:
                    u2 += gra[i][j]
                else:
                    u3 += gra[i][j]

                if i <= x:
                    d1 += gra[i][j]
                elif i > x and j <= y:
                    d2 += gra[i][j]
                else:
                    d3 += gra[i][j]
            


        
        res = max(res, s1*s2*s3)
        res = max(res, a1*a2*a3)
        res = max(res, u1*u2*u3)
        res = max(res, d1*d2*d3)
print(res)




"""
# X = 0 | 1,2
   
   왼쪽
       0 | 1 2    
y=0     ㅡ
       3 | 4 5
y=1     ㅡ
       6 | 7 8
   
   
   오른쪽
       0 | 1 2
          ㅡㅡㅡ
       3 | 4 5
          ㅡㅡㅡ
       6 | 7 8
   
   
# 0, X = 1 | 2
       
       왼쪽
       0 1 | 2
 y=0  ㅡㅡㅡ
       3 4 | 5
 y=1  ㅡㅡㅡ
       6 7 | 8


       
       오른쪽
       0 1 | 2
 y=0       ㅡㅡㅡ
       3 4 | 5
 y=1       ㅡㅡㅡ
       6 7 | 8


# Y = 0
  ㅡㅡㅡㅡㅡ
  1
  2
  
  위   0 | 1 | 2
       ㅡㅡㅡㅡㅡ
 아래  3 | 4 | 5
       6 | 7 | 8

# 0
  Y = 1
  ㅡㅡㅡㅡㅡ
  2
  
  위  0 | 1 | 2
       3 | 4 | 5
      ---------
아래 6 | 7 | 8
    


"""
