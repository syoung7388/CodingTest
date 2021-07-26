if __name__ == "__main__":
    gra = [list(map(int, input().split())) for _ in range(7)]
    cnt = 0

    for i in range(7):
        for s in range(3):
            if gra[i][s] == gra[i][s+4] and gra[i][s+1] == gra[i][s+3]:
                cnt += 1
            if gra[s][i] == gra[s+4][i] and gra[s+1][i] == gra[s+3][i]:
                cnt += 1
    print(cnt)


    
    """
    for i in range(7):
        for j in range(7):
            if j+4 < 7 and gra[i][j] == gra[i][j+4]:
                if gra[i][j+1] == gra[i][j+3]:
                    cnt += 1
            if i+4 <7 and gra[i][j] == gra[i+4][j]:
                if gra[i+1][j] == gra[i+3][j]:
                    cnt += 1
        print(cnt)
    """


    
