
N = int(input())
nums = [0]*(N+1)
cnt = 0
for i in range(2, N+1):
    if nums[i] == 0:
        cnt += 1
        for j in range(i, N+1, i): #3번째 step
            nums[j] =1
print(cnt)




""" #시간 초과
N= int(input())
aws = 0
for i in range(2,N+1):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
        if count > 2:
            break
    else:
        aws += 1
print(aws)

"""



