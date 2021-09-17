import math

for _ in range(int(input())):
    x, y = map(int, input().split())
    dis = y-x #3
    
    n =int(math.sqrt(dis))
    
    if dis <= 3:
        print(dis)
    elif dis  == n**2:
        print(n*n-1)
    elif n**2 < dis <= n**2+n:
        print(n*n)
    else:
        print(n*n+1)
