#암호화





def DFS(L, P):
    global cnt
    if L == N:
        cnt +=1
        for c in range(P):
            print(chr(p[c]+64), end="")
        print()
        return
    else:
        for i in range(1, 27):
            if i <10 and i == nums[L]:
                p[P] = i
                DFS(L+1, P+1)
            
            elif i >= 10 and L+1 < N and i%10 == nums[L+1] and i//10 == nums[L]:
                p[P] = i
                DFS(L+2, P+1)



if __name__ == "__main__":

    nums = list(map(int, input()))
    N = len(nums)
    p = [0]*(N+3)
    cnt = 0

    DFS(0,0)
    print(cnt)
        
    

    
