


def chNum(m):
    cnt = 0
    for i in range(K):
        cnt += Sun[i]//m
    return cnt


if __name__ == "__main__":
    K, N = map(int, input().split())
    Sun = list(int(input()) for _ in range(K))

    lt = 1
    rt = max(Sun)
    res = 0
    while lt <= rt:
        mid = (lt+rt) // 2
        num = chNum(mid)

        if num >= N:
            res = max(res, mid)
            lt = mid+1
        else:
            rt = mid-1
    print(res)
            
    
