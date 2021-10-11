

Max = int(input()) #맥스레벨
avatar = list(map(int, input().split())) #레벨별 캐릭터 수
him = list(map(int,  input().split())) #캐릭터별 수
D = int(input())
N = len(avatar)
S = 0

            
dp  = [[0]*(D+1) for _ in range(N)]

for i in range(N):

    S += avatar[i]*him[i]


for i in range(N):
    dp[i][0] = S


for i in range(1, N):
    num = avatar[i-1]
    cha = him[i]-him[i-1]
    for j in range(1, D+1):
        if dp[i-1][j] < dp[i][j-1]+cha:
            avatar[i-1] -= 1
            dp[i][j] = dp[i][j-1]+cha
        else:
            dp[i][j] = dp[i-1][j]
        if avatar[i-1] == 0:
            break
for d in dp:
    print(d)

print()
print(avatar)
        
