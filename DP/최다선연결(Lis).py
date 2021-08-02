N = int(input())

nums = list(map(int, input().split()))
nums.insert(0,0) # 1~

dy = [0]*(N+1)
dy[1] = 1
for i in range(2, N+1): #기준 번호

    bf = 0
    for j in range(1, i): #앞번호
        if nums[j] < nums[i] and  dy[j] > bf:
            bf = dy[j]
    dy[i] = bf+1

print(max(dy))
