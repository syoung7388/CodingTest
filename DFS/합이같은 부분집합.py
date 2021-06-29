import sys

def DFS(L, add):
    if add > total//2:
        return
    if L == N:
        if (total-add) == add:
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1, add+ nums[L])
        DFS(L+1, add)


if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))
    total = sum(nums)
    DFS(0,0)
    print("NO")
