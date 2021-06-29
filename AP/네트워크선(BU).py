# 1m, 2m - 선자르기 // 부분증가수열의 최대길이 // BU

N = int(input())

dy = [0]*(N+1) #for 1~
dy[1] = 1
dy[2] = 2

for i in range(3, N+1):
    dy[i] = max(dy[i], dy[i-2]+dy[i-1])
print(dy[N])
    



