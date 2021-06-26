N = int(input())
nums= [list(map(int, input().split())) for _ in range(N)]

M = int(input())

for m in range(M):
    r, geo, move = map(int, input().split())
    for i in range(move):
        if geo == 0:
            nums[r-1].append(nums[r-1].pop(0))
        else:
            nums[r-1].insert(0,nums[r-1].pop())

n = 0
e = N
add = 0
for j in range(len(nums)):
    for l in range(n,e):
        add += nums[j][l]

    if j < N//2:
        n += 1
        e -= 1
    else:
        n -= 1
        e += 1
print (add)
        
