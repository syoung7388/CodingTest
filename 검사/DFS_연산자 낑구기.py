def DFS(L,sum):
    global Max
    global Min
    if L == N:
        if Max < sum:
            Max = sum
        if Min > sum:
            Min = sum
        return
    else:
        for i in range(4):
            if buho[i] > 0:
                buho[i] -= 1
                if i == 0:
                    DFS(L+1, sum+nums[L])
                elif i == 1:
                    DFS(L+1, sum-nums[L])
                elif i == 2:
                    DFS(L+1, sum*nums[L])
                elif i == 3:
                    if sum <0 :
                        DFS(L+1, -(-sum//nums[L]))
                    else:
                        DFS(L+1, sum//nums[L])
                        
                buho[i]+=1
                


if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))
    buho = list(map(int, input().split()))
    Max = -2147000000
    Min = 2147000000
    DFS(1, nums[0])
    print(Max)
    print(Min)
