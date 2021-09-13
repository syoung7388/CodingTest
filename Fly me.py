import math
for _ in range(int(input())):
    x, y = map(int,input().split())
    dis = y-x
    if dis <= 3:
        print(dis)
        continue
    n = int(math.sqrt(dis))

    if dis == n**2:
        print(2*n-1)
    elif n**2 < dis <= n**2+n:
        print(2*n)
    else:
        print(2*n+1)
