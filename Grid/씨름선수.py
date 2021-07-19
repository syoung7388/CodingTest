if __name__ == "__main__":
    N = int(input())
    can = [list(map(int, input().split())) for _ in range(N)]
    can.sort(reverse = True)
    cnt = 0
    largest = 0
    for x, y in can:
        if y > largest:
            cnt += 1
            largest = y
    
    print(cnt)
        
    
    
    
                
