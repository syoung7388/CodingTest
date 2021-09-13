import math


for _ in range(int(input())):
    s, e = map(int,input().split())
    dis= e-s
    if dis <= 3:
        print(dis)
        continue
        
    n =int(math.sqrt(dis))

    if dis == n**2:
        print(n**2-1)
    elif n**2 < dis <= (n**2)+n:
        print(n**2)
    else:
        print(n**2+1)
    
    
