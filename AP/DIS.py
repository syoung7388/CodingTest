#플로이드 워샬 알고리즘

N,M = map(int, input().split()) #도시개수 #도로수

dy = [[500]*(N+1) for _ in range(N+1)]

for c in range(M):
    c1, c2, k = map(int, input().split()) 
    dy[c1][c2] = k
for i in range(1, N+1):
    dy[i][i] = 0
for k in range(1, N+1):    
    for i in range(1, N+1): 
        for j in range(1,N+1):
            dy[i][j] = min(dy[i][j], dy[i][k]+dy[k][j])
            
for a in range(1, N+1):
    for w in range(1, N+1):
        if dy[a][w] == 500:
            dy[a][w] = "M"
        print(dy[a][w], end=" ")
    print()

        
        
    
    
