N = int(input())
nums = list(map(int, input().split()))
nums.insert(0,0) #1~
aws = [0]*(N+1) #1~
aws[1] = 1


for i in range(2, N+1):
    bf = 0
    for j in range(1, i): 
        if nums[j] < nums[i] and aws[j]>bf:
            bf = aws[j]
    aws[i] = bf+1          
 
print(max(aws))
