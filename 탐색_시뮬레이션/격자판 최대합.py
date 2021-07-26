N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]


bf = -2147000000
sum3 = sum4 = 0
for i in range(N):
    sum1 = sum2 = 0
    sum3 += nums[i][i]
    sum4 += nums[N-1-i][i]
    for j in range(N):
        sum1 += nums[i][j]
        sum2 += nums[j][i]
    if sum1 > bf:
        bf = sum1
    if sum2 > bf:
        bf = sum2
if sum3 > bf:
    bf = sum3
if sum4 > bf:
    bf = sum4
print(bf)
