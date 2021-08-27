from __future__ import division
import math


N = int(input())
points = list(map(int, input().split()))
K = int(input())

BIT = 64            #ULL 변수를 bool 배열로 활용
bitmask = 1132502
#print(bitmask)
mask = 2**BIT -1
# score: i번 부터 j번까지 맞췄을때 점수 합
score = [[0 for _ in range(N + 2)] for _ in range(N + 2)]
# sum: i번부터 j번까지의 배점의 합
sum = [0 for _ in range(N + 2)]

for i in range(1, N + 1):
    sum[i] = sum[i-1] + points[i - 1]
for i in range(1, N+1):
    for j in range(i, N+1):
        score[i][j] = score[i][j-1] + sum[j] - sum[i-1]


# dp[i][j] : 0 ~ i번까지 고려했을 때 j가 정답이 될 수 있는지
dp = [[0 for _ in range(int(bitmask / BIT))] for _ in range(N + 1)]

def set_bit(row, k):
    r = int(k / BIT)
    c = int(k % BIT)
    dp[row][r] = (dp[row][r] | 1 << c) & mask
    #print(dp[row][r])

def check_bit(row, k):
    r = int(k / BIT)
    c = int(k % BIT)
    return dp[row][r] & (1 << c)

# pre: 이전까지 고려한 문제, cur: 지금 포함된 마지막 문제 k: score값
def fill_bit(pre, cur, k):
    #row가 될수 있는 값의 범위 (1번부터 pre번 까지 다 맞았을 때의 값으로 계산)
    preMax_r = int(score[1][pre] / BIT)
    r = int(k / BIT)
    c = int(k % BIT)
    # c가 0보다 크다면
    if c > 0:
        for i in range(preMax_r + 1):
            dp[cur][i+r] = (dp[cur][i+r] | (dp[pre][i] << c)) & mask
            dp[cur][i+r+1] = (dp[cur][i+r+1] | (dp[pre][i] >> (BIT-c))) & mask
    else:
        for i in range(preMax_r + 1):
            dp[cur][i+r] = (dp[cur][i+r] | (dp[pre][i] << c)) & mask

def solve():
    # 만약 K가 모두 맞은것보다 크다면 답은 K가 됨
    if (K > score[1][N]):
        print(K)
        return

    set_bit(0, 0)
    #첫 문제만 봐서 맞춘것과
    set_bit(1, points[0])
    #못맞춘것 set
    set_bit(1, 0)

    for i in range(2, N + 1):
        for j in range(1, i + 2):
            if j <= 2:
                set_bit(i, score[j][i])
            else:
                fill_bit(j-2, i, score[j][i])

    ans = K
    while check_bit(N, ans):
        ans += 1
    print(ans)
    return

solve()
