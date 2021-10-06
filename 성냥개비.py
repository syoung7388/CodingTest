

import sys
input = sys.stdin.readline


nums= {2:1, 3:7, 4:4, 5:2, 6:6, 7:8}


for _ in range(int(input())):
    N = int(input())
    cnt = (N-1)//7
    if N == 6:
        small = 6
    elif N <= 7:
        small = nums[N]
    else:
        if N%7 == 1:
            small = int("10"+("8"*((N//7)-1)))
        elif N%7 == 3:
            if N == 10:
                small = 22
            else:
                small = int("200"+("8"*((N//7)-2)))
        elif N%7 == 4:
            small = int("20"+("8"*((N//7)-1)))
        else:
            a = N%7 if N%7 else 7
            small = int(str(nums[a]) +("8"*cnt))
    cnt = N//2
    if N%2 == 0:
        large = int("1"*cnt)
    else:
        large = int("7"+ "1"*(cnt-1))
    print(small, large)











"""
import math
Max = math.inf
ndp = [Max]*(101)
xdp = [0]*(101)
ndp[2] = xdp[2] = 1
ndp[3] = xdp[3] = 7
ndp[4] = 4
ndp[5] = 2
ndp[6] = 0
ndp[7] = 8

for _ in range(int(input())):
    N = int(input())

    for i in range(2, N+1):
        if ndp[i] != Max: continue
        for j in range(2, i-1):
            arr = str(ndp[j])+str(ndp[i-j])

            for _ in range(len(arr)):
                arr = arr[::-1]
                temp = arr
                if arr[0] == '0':
                    arr='6'+arr[1:]
                if int(arr) < ndp[i]:
                    ndp[i] = int(arr)
                arr = temp
    for i in range(2, N+1):
        if xdp[i] != 0: continue      
        for j in range(2, i-1):
            arr = str(xdp[j])+str(xdp[i-j])
            for _ in range(len(arr)):
                arr = arr[::-1]
                if int(arr) > xdp[i]:
                    xdp[i] = int(arr)
    print(N, end = ":")
    if N == 6:
        print(6, xdp[N])
    else:
        print(ndp[N], xdp[N])
"""
