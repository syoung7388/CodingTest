import sys
import math


def getIdx(n):
    return (n-fir[K])/d[K]+1

left = int(input())
right = int(input())
K = int(input())
fir = {2:3, 3:6, 4:14, 5:15}
d = {2:1, 3:3, 4:2, 5:5}


if left == right :

    arr = getIdx(left)

    if left >= fir[K] and arr == int(arr):
        print(1)

    elif K == 4 and left == 10: #10 10 4 => 무조건 1
        print(1)

    else:
        print(0)

    sys.exit(0)

if left <= fir[K]:
    lt = 1
else:
    lt = math.ceil(getIdx(left))
    
rt = int(getIdx(right))


res = max(rt - lt +1, 0)

if K == 4 and left <= 10 and right >= 10:
    res += 1

print(res)



