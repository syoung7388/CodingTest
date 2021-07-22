





def Count(m):
    s = 0
    cnt = 1
    for i in range(N):
        if s+music[i] > m:
            cnt += 1
            s = music[i]
        else:
            s += music[i]
    return cnt


if __name__ == "__main__":
    N, M = map(int, input().split())
    music = list(map(int, input().split()))


    lt = max(music)
    rt = sum(music)
 
    while lt <= rt:
        mid = (lt+rt) // 2
        if Count(mid) <= M:
            res = mid
            rt = mid-1
        else:
            lt = mid+1

    print(res)
            

        


    
