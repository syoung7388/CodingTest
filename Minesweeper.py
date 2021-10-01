dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]


for _ in range(int(input())):
    N = int(input())
    if N <= 2:
        a = [list(map(int, input())) for _ in range(N)]
        print(0)
        continue

    gra = [list(map(int, input()))]
    
    
    for _ in range(N-2):
        arr = input()
        gra.append([int(arr[0])]+[-1]*(N-2)+[int(arr[-1])])
    gra.append(list(map(int, input())))

    Q = set()
    for i in range(1, N-1):
        Q.add((1, i))
        Q.add((i, 1))
        Q.add((i, N-2))
        Q.add((N-2, i))

    
    res = 0
    while Q:
        x, y = Q.pop()
        temp = []
        for k in range(8):
            xx, yy = x + dx[k], y + dy[k]
            if not (xx == 0 or yy == 0 or xx == N-1 or yy == N-1): continue
            if gra[xx][yy] -1 < 0:
                break
            temp.append((xx, yy))
        else:
            res += 1
            for tx, ty in temp:
                gra[tx][ty] -= 1


    if N < 5:
        plus = 0
    else:
        plus = (N-4)*(N-4)
    print(res+plus)
