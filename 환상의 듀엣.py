

import math
N = int(input())
H = [0]+list(map(int, input().split()))

dp = [[math.inf]*(N+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(N): #덕이
    for j in range(N):#원이
        next = max(i, j)+1

        print(i, j)

        # 덕이가 음을 바꾸기
        plus = abs(H[i]-H[next]) if i != 0 else 0 #i = 0일때
        dp[next][j] = min(dp[next][j], dp[i][j]+plus)

        for d in dp:
            print(d)
        print()

        #원이가 음을 바꾸는 경우

        plus = abs(H[j]-H[next]) if j != 0 else 0
        dp[i][next] = min(dp[i][next], dp[i][j]+plus)
        for d in dp:
            print(d)
        print()



for d in dp:
    print(d)
print()


print(min(min(dp[N]), min(row[N] for row in dp)))

