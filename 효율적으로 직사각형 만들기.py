N, M = map(int, input().split())
arr = [[0]*M for _ in range(N)]

for i in range(N):
    for j, k in enumerate(map(int, input())):
        if  i == 0:
            arr[i][j] = arr[i][j-1]+k
        elif j == 0:
            arr[i][j] = arr[i-1][j]+k
        else:
                                                    #겹치는 부분
            arr[i][j] = arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1] + k

res = 0

for i in range(N-1):
    for j in range(M-1):
        
        #1)  |
        #  ㅡㅡㅡㅡㅡ
        a, b, c = arr[i][j],(arr[i][M-1]-arr[i][j]), (arr[N-1][M-1]-arr[i][M-1])
        res = max(res, a*b*c)

        #2)ㅡㅡㅡㅡㅡ  
        #    |
        a, b, c = arr[i][-1], (arr[-1][j]-arr[i][j]), (arr[-1][-1]-arr[i][-1]-(arr[-1][j]-arr[i][j]))
        res = max(res, a*b*c)


        #3)    |
        #    --|
        #      |

        a, b, c = arr[i][j], arr[N-1][j]-arr[i][j], arr[N-1][M-1] - arr[N-1][j]
        res = max(res, a*b*c)
        
        #4)    |
        #      |--
        #      |

        a, b, c = arr[-1][j], arr[i][-1] - arr[i][j], arr[-1][-1] - arr[-1][j] - (arr[i][-1] - arr[i][j])
        res = max(res, a*b*c)


#3) ---
#   ---
#   ---

for x1 in range(N-2):
    for x2 in range(x1+1, N-1):
        a, b, c = arr[x1][-1], arr[x2][-1] - arr[x1][-1], arr[-1][-1] - arr[x2][-1]
        res = max(res, a*b*c)
#3) | |
#   | |
#   | |

for y1 in range(M-2):
    for y2 in range(y1+1, M-1):
        a, b, c = arr[-1][y1], arr[-1][y2] - arr[-1][y1], arr[-1][-1] - arr[-1][y2]
        res = max(res, a*b*c)
    
        
print(res)

        
