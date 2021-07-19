





def digit_sum(x):

    sum = 0
    while x > 0:
        sum += x%10
        x= x//10

    return sum

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))
    bf = -2147000000
    res = 0
    for i in range(N):
        tot = digit_sum(nums[i])
        if tot > bf:
            bf = tot
            res = nums[i]
    print(res)
            
