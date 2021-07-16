
def Count(m):
    s = 0
    cn = 1
    for v in MV:
        if s + v > mid:
            cn += 1
            s = v
        else:
            s += v
    return cn
        

if __name__ == "__main__":
    N, M = map(int, input().split())
    MV = list(map(int, input().split()))
    S = sum(MV)

    lt = max(MV)
    rt = S
    while lt < rt:
        mid = (lt+rt) // 2
        cnt = Count(mid)
        if cnt <= M:
            res = mid
            rt = mid-1
        else:
            lt = mid+1

    print(res)
            
            
            
    
