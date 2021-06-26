N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]
nums.sort()
nums.insert(0,[0]*3)
dy = [0]*(N+1)
dy[1] = nums[1][1] #0번째 길이 미리 넣기


for i in range(2, N+1): #현재 2~5
    bf = 0
    for j in range(1, i): #구버전 1~4
        if nums[j][2] < nums[i][2] and dy[j]> bf:
            bf = dy[j]
    dy[i]= bf+nums[i][1]

print(max(dy))    
    
