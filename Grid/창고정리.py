
#가장 높은 곳과 낮은 곳의 차이?


if __name__ == "__main__":
    R = int(input())
    H = list(map(int, input().split()))
    C = int(input())
    cnt = 0
    while True:
        H.sort()
        if cnt == C:
            break
        cha = min(H[R-1]-H[R-2], H[1]-H[0])+1
        if cnt + cha >= C:
            cha = C-cnt
        H[0] += cha
        H[R-1] -= cha
        cnt += cha
    print(H[R-1]-H[0])

    
    
