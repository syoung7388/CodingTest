
#행, 0:왼쪽 , 3만큼 회전 // 모래시계 출력


if __name__ == "__main__":
    N = int(input())
    gra = [list(map(int, input().split())) for _ in range(N)]

    M = int(input())

    for _ in range(M):
        h, b ,move = map(int, input().split())

    
        for _ in range(move):
            if b == 0:
                gra[h-1].append(gra[h-1].pop(0))
            else:
                gra[h-1].insert(0, gra[h-1].pop())


    lt = 0
    rt = N-1
    S  = 0

    for i in range(N):
        for j in range(lt, rt+1):
            S += gra[i][j]
        if i < N//2:
            lt += 1
            rt -= 1
        else:
            lt -= 1
            rt += 1
    print(S)
