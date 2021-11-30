import sys
input = sys.stdin.readline

def spring_summer():
    for i in range(N):
        for j in range(N):
            if gra[i][j]:
                temp = {}
                die = 0
                
                for y in sorted(gra[i][j].keys()):
                    if y*gra[i][j][y]<=water[i][j]:
                        temp[y+1] = gra[i][j][y]
                        water[i][j] -= y*gra[i][j][y]
                    else:

                        survive = water[i][j] // y
                        if not survive:
                            die += (y//2)*gra[i][j][y]
                        else:
                            water[i][j] -= y*survive
                            temp[y+1] = survive
                            die += (y//2)*(gra[i][j][y] - survive)
                            
                gra[i][j] = temp
                water[i][j] += die
def fall():
    
    for i in range(N):
        for j in range(N):
            if gra[i][j]:
                cnt = 0
                for a in gra[i][j].keys():
                    if a%5 == 0:
                        cnt += gra[i][j][a]
                if cnt:
                        
                    for k in range(8):
                        xx, yy = dx[k]+i, dy[k]+j
                        if not (0<=xx<N and 0<=yy<N): continue
                        if 1 in gra[xx][yy]:
                            gra[xx][yy][1] += cnt
                        else:
                            gra[xx][yy][1] = cnt


dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
N, M, K = map(int, input().split())
arr =  [list(map(int, input().split())) for _ in range(N)]
water = [[5]*N for _ in range(N)]
gra = [[{} for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())
    gra[x-1][y-1][z] = 1

    
for _ in range(K):
    #순서1) 양분먹기, 나이증가, 죽은나무 처러, 번식 나무 구하기
    breed = []
    spring_summer()
    #순서2) 번식하기
    fall()
     
    
    #양분 채우기    
    for i in range(N):
        for j in range(N):
            water[i][j] += arr[i][j]

  


res = 0

for i in range(N):
    for j in range(N):
        if gra[i][j]:
            res += sum(gra[i][j].values())
print(res)
