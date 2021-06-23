#카드 3장, K번째 수

N, K = map(int,input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True)
sums = set()

for i in range(N):
    for j in range(i + 1, N):
        for c in range(j + 1, N):
            sums.add(nums[i] + nums[j] + nums[c])

sums = list(sums)
sums.sort(reverse=True)
print(sums[K-1])



""" 틀린답 3장 뽑을때는 다 더하고 판단해야함 !! 배운점 이중 for문은 break 여러번 걸던가 혹은 Exception 
try:
    for i in range(N):
        for j in range(i+1, N):
            for c in range(j+1, N):
                sums.add(nums[i]+nums[j]+nums[c])
                if len(sums) == K:
                    raise NotImplementedError
except:
    sums = list(sums)
    sums.sort(reverse=True)
    print(sums)
    print(sums[K-1])
"""





"""
10 3
13 15 34 23 45 65 33 11 26 42

30 7
23 26 50 17 34 35 50 22 53 41 42 44 43 49 37 50 28 31 15 37 38 33 48 40 17 42 29 53 23 3

"""
