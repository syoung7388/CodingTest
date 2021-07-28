import sys


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    if max(arr) >= M:
        print(1)
        sys.exit(0)

        
    lt = 0
    rt = 1
    Sum = arr[0]+arr[1]
    Len = N+1
    while lt <= rt:
        if Sum >= M:
            l = rt - lt +1  
            if l < Len:
                Len = l
            Sum -= arr[lt]
            lt += 1
        else:
            rt += 1
            if rt >= N:
                break
            Sum += arr[rt]
    if Len == N+1:
        print(0)
    else:
        print(Len)
        
            
        


 
