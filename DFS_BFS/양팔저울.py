


def DFS(L, sum):
    if L == N:  
        if 0 < sum <= S:
            aws.add(sum)
    else:
        DFS(L+1, sum+nums[L])
        DFS(L+1, sum-nums[L])
        DFS(L+1, sum)

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))
    S = sum(nums)
    aws = set()
    DFS(0,0)
    print(S - len(aws))

  
                
                
                
            
        

    
    
