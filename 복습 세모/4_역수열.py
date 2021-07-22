

if __name__ == "__main__":
    N = int(input())
    yul = list(map(int, input().split()))
    ch = [0]*N

    for i in range(N):
        for j in range(N):
            if yul[i] == 0 and ch[j] == 0:
                ch[j] = i+1
                break
            if ch[j]== 0:
                yul[i] -= 1
                
    for c in ch:
        print(c, end=" ")
    
