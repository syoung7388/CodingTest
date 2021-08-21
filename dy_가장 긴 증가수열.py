N = int(input())
nums = list(map(int, input().split()))
dy = [0]*(N)
mv = [0]*(N)
dy[0] = 1
for i in range(1, N):
    bf = 0
    n = i
    for j in range(i):
        if nums[j] < nums[i] and dy[j]>bf:
            bf =dy[j]
            n = j
    dy[i] = bf+1
    mv[i] = n

idx = dy.index(max(dy))
print(dy[idx])
lo = idx
res = ""
for _ in range(dy[idx]):
    res = str(nums[lo])+" "+res
    lo = mv[lo]
print(res)
