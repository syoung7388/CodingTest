import sys

n, m = map(int, sys.stdin.readline().split())

data = [(0, 0)]
light = [0]
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    data.append((a, b))
    light.append(light[-1] + b)

dp = [[[float('inf'), float('inf')] for _ in range(n + 1)] for _ in range(n + 1)]
dp[1][n][0] = dp[1][n][1] = 0


def f(i, j, flag):
    if dp[i][j][flag] < float('inf'):
        return dp[i][j][flag]

    if flag:
        cur = data[j][0]
    else:
        cur = data[i][0]

    left = float('inf')
    right = float('inf')
    on = light[n] - light[j] + light[i - 1]

    if i > 1:
        left = f(i - 1, j, 0) + (cur - data[i - 1][0]) * on

    if j < n:
        right = f(i, j + 1, 1) + (data[j + 1][0] - cur) * on

    dp[i][j][flag] = min(left, right)
    return dp[i][j][flag]


print(f(m, m, 0))
