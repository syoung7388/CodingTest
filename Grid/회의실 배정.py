




if __name__ == "__main__":
    n = int(input())
    time = [list(map(int, input().split())) for _ in range(n)]
    time.sort(key = lambda x : (x[1] , x[0]))
    cnt = 1
    lo = time[0]
    for i in range(1, n):
        if lo[1] <= time[i][0]:
            cnt += 1
            lo = time[i]
    print(cnt)
            
            
