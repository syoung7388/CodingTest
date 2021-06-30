

def DFS(id, s, add):
    global cnt
    if add > tot:
        return
    elif id ==K:
        if add % M == 0:
            cnt+=1
        return
    else:
        for i in range(s, N+1):
            DFS(id+1, i+1, add+nums[i])
if __name__ == "__main__":
    N, K = map(int, input().split()) # 숫자 수 .. 몇개 뽑는지
    nums = list(map(int, input().split()))
    nums.insert(0,0)
    tot = sum(nums)
    cnt = 0
    
    M = int(input()) #배수 수

    DFS(0, 1, 0)
    print(cnt)
