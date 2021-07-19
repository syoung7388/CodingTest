if __name__ == "__main__":
    N = int(input())
    a = list(map(int, input().split()))

    ch = [0]*(N)
    
    for i in range(N):
        for j in range(N):
            if a[i] == 0 and ch[j] == 0:
                ch[j] = i+1
                break
            elif ch[j] == 0:
                a[i] -= 1
    for c in ch:
        print(c, end=" ")
                
                
                       
        
