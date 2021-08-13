
def DFS(now):
    ch[now] = 1
    if ch[nums[now]] == 0:
        DFS(nums[now])
for _ in range(int(input())):
    N = int(input())
    nums = list(map(int, input().split()))
    nums.insert(0, 0)
    cnt = 0
    ch = [0]*(N+1)
    for i in range(1, N+1):
        if ch[i] == 0:
            cnt += 1
            DFS(i)
    print(cnt)
