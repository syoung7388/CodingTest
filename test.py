
N = int(input())
nums = list(map(int, input().split()))

arr = []
arr.append(min(nums[0], nums[5]))
arr.append(min(nums[1], nums[4]))
arr.append(min(nums[2], nums[3]))
arr.sort()

mins1, mins2, mins3 = arr[0], arr[0]+arr[1], arr[0]+arr[1]+arr[2]

cnt1 = (N-2)**2 + (N-2)*(N-1)*4
cnt2 = (N-2)*4 + 4*(N-1)
cnt3 = 4
s = mins1*cnt1 + mins2*cnt2 + mins3*cnt3
print(s)
