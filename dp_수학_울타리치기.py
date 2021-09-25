i = int(input()) / 6
print(int(3*i*(i+1)+1))














""" #내가 제출한 정답 dp 이용
import sys

N = int(input())
if N < 6:
    print(N)
    sys.exit(0)

dp = [0]*(1000001)
dp[6] = 7
dp[7] = 8
dp[8] = 10
dp[9] = 12
dp[10] = 14
dp[11] = 16

if N > 11:
    for i in range(12, N+1):
        dp[i] = i+dp[i-6]
print(dp[N])
    
"""
