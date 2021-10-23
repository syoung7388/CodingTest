import sys

tot_dp = [0]*(31)
sym_dp = [0]*(31)


N = int(input())

if N == 1 or N == 2:
    print(tot_dp[N])
    sys.exit(0)
    
    
tot_dp[1] = 1
tot_dp[2] = 3
for i in range(3, N+1):
    tot_dp[i] = tot_dp[i-2]*2 + tot_dp[i-1]




sym_dp[1] = 1
sym_dp[2] = 3
sym_dp[3] = 1
sym_dp[4] = 5

for i in range(5, N+1):
    sym_dp[i] = sym_dp[i-2] + 2 * sym_dp[i-4]

print(tot_dp)
print(sym_dp)

print((tot_dp[N] - sym_dp[N])//2 + sym_dp[N])
