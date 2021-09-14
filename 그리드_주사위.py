import sys


N = int(input())
nums = list(map(int, input().split()))


if N == 1:
    print(sum(nums) - max(nums))
    sys.exit(0)


mins = [0]*(4)
n_list = []

n_list.append(min(nums[0], nums[5]))
n_list.append(min(nums[1], nums[4]))
n_list.append(min(nums[2], nums[3]))

n_list.sort()
mins[1] = n_list[0]
mins[2] = n_list[0]+n_list[1]
mins[3] = n_list[0]+n_list[1]+n_list[2]


dic = {3:4 , 2:0, 1:0}
dic[2] = (N-2)*4 +(N-1)*4
dic[1] = (N-2)**2 + 4*(N-2)*(N-1)

res = 0
for k, v in dic.items():
    res += mins[k]*v
print(res)
    


