import sys
input = sys.stdin.readline

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a%b)

N = int(input())
nums = [int(input()) for _ in range(N)]

for i in range(N-1):
    nums[i] = abs(nums[i+1] - nums[i])
nums.pop()


number = nums[0]
for n in nums:
    number = gcd(number, n)
res= set([number])


for i in range(2, int(number**(1/2))+1):
    if number%i == 0:
        res.add(i)
        res.add(res//i)
print(' '.join(map(str, sorted(res))))
