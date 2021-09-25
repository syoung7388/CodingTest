
def DFS(cnt, remain):
    global bf
    if cnt > bf:
        return
    if remain == 0:
        if cnt < bf:
            bf = cnt
        return
    elif remain < 0:
        return
    else:
        for i in range(N):
            DFS(cnt+1, remain-coins[i])
if __name__ == "__main__":    
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    coins.sort(reverse=True)
    cnt = 0
    bf = 501
    remain = M
    DFS(0, remain)
    print(bf)

