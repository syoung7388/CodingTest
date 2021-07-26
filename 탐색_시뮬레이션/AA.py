N, M= map(int, input().split())
nums = list(map(int, input().split()))
count = 0
sum = 0
i = 0
skip =0
while i < N:
    if sum == M:
        count += 1
        i -= 1
        skip = 0
        sum = 0
    elif sum > M:
        i = i - skip -1
        sum = 0
        skip = 0
    elif sum < M:
        sum += nums[i]
        i += 1
        skip += 1


print(count)

