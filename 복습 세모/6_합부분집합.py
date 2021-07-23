
import sys


def DFS(L, S):

    if S > total//2:
        return
    if (total - S) == S:
        print("YES")
        sys.exit(0)
    
    if L == N:
        return
    DFS(L+1, S+nums[L])
    DFS(L+1, S)
    
    





if __name__ == "__main__":
    sys.setrecursionlimit(10**7) 
    N = int(input())
    nums = list(map(int, input().split()))

    total = sum(nums)

    DFS(0, 0)

    print("NO")
