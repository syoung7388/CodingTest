dic = {2:1, 3:7, 4:4, 5:2, 6:6, 7:8}

for _ in range(int(input())):
    N = int(input())
    
    if N <= 7:
        small = dic[N]
    elif N%7 == 1:
        small = '10'+'8'*(N//7-1)
    elif N%7 == 3:
        if N == 10:
            small = 22
        else:
            small = '200' + '8'*(N//7-2)
    elif N%7 == 4:
        small = '20'+'8'*(N//7-1)
    else:
        a = N%7 if N%7 else 7
        b = N//7 if N%7 else N//7-1
        small = str(dic[a]) + '8'*(b)
    cnt = N//2
    if N%2 == 0:
        large = '1'*(cnt)
    else:
        large = '7'+'1'*(cnt-1)
    print(small, large)
