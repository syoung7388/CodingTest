N = int(input())
C = list(map(int, input().split()))
M = int(input())
dy = [550]*(M+1)
dy[0]=0

for i in range(N):
    for j in range(C[i], M+1):
        dy[j] = min(dy[j-C[i]]+1, dy[j])
print(dy[M])
