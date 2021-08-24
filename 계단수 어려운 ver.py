import sys


def Move(bit, d, l):
    if l <0 or l > 9:
        return 0
    if d == N: #자릿수가 끝이라면
        if bit == (1<<10)-1:
            print(bin(bit))
            return 1
        else:
            return 0
    if dp[bit][d][l] != -1:
        return dp[bit][d][l]
    dp[bit][d][l] = 0

    if l == 0:
        dp[bit][d][l] += Move(bit | (1<<(l+1)), d+1, l+1)
        dp[bit][d][l] %= m
    elif l  == 9:
        dp[bit][d][l] += Move(bit | (1<<(l-1)), d+1, l-1)
        dp[bit][d][l] %= m

    else:
        dp[bit][d][l] += Move(bit | (1<<(l+1)), d+1, l+1)
        dp[bit][d][l] %= m
        dp[bit][d][l] += Move(bit | (1<<(l-1)), d+1, l-1)
        dp[bit][d][l] %= m
    return dp[bit][d][l]

m = 1000000000
N = int(sys.stdin.readline())
dp = [[[-1]*(11) for _ in range(101)] for _ in range(1<<11)]

res = 0
for i in range(1, 10):
    res += Move(1<<i, 1, i)
    res %= m
print(res)
