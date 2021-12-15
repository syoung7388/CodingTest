def roll(n, x, y, size, step, flag):


    gra = [[0]*n for _ in range(n)]
    idx = n**2
    while True:
        for _ in range(size):
            idx -= 1
            x += step
            if not flag:
                gra[x][y] = arr[idx]
            else:
                gra[y][x] = arr[idx]
            
        size -= 1
        if size < 1 : break
        
        if not flag: step = -step
        
        for _ in range(size):
            idx -= 1
            y += step
            if not flag:
                gra[x][y] = arr[idx]
            else:
                gra[y][x] = arr[idx]

        if flag: step = -step

    return gra
