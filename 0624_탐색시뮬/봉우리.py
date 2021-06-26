N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]

nums.append([0]*N)
nums.insert(0, [0]*N)
for z in nums:
    z.append(0)
    z.insert(0,0)


dx = [-1,0,1,0]
dy= [0,1,0,-1]

cnt = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if all(nums[i][j] > nums[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1
print(cnt)
