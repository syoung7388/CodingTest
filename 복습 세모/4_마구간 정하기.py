
def Count(m):

    cnt = 1
    ep = bang[0]
    for b in range(1, N):
        if bang[b] - ep >= m:
            cnt += 1
            ep = bang[b]
    return cnt
        


if __name__ == "__main__":
    N, C = map(int, input().split())

    bang = list(int(input()) for _ in range(N))

    bang.sort()

    lt = 1
    rt = bang[N-1]
    while lt <= rt:
        mid = (lt+rt) //2
        if Count(mid) >= C:
            res = mid
            lt = mid+1
        else:
            rt = mid-1


    print(res)
