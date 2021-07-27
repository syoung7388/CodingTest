
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    if max(nums) >= M:
        print(1)
        sys.exit(0)

    lt = 0
    rt = 1
    res = N+1
    Sum = nums[0]+nums[1]
    while lt <= rt:
        print(lt, rt, Sum)
        if Sum >= M:
            res= min(res, rt-lt+1)
            Sum -= nums[lt]
            lt += 1

        else:
            rt += 1
            if rt >= N:
                break
            Sum += nums[rt]
        
            
    if res == N+1:
        print(0)
    else:
        print(res)
    
            
        


 
