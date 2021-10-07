import sys
from collections import deque
import math
input = sys.stdin.readline


def GCD(a, b):
    if a%b == 0:
        return b
    return GCD(b, a%b)

ex, ey = map(int, input().split())
cx, cy , px, py = map(int, input().split())

if px == 0 and py == 0:
    print(cx, cy)
    sys.exit(0)
elif py == 0:
    px = 1 if px > 0 else -1
elif px == 0:
    py = 1 if py > 0 else -1
else:    
    nums = abs(GCD(px, py))
    if  nums != 1:
        px, py = px//nums, py//nums
        

Q = deque([(cx, cy)])

mdis = math.inf
res = ()
while Q:
    x, y = Q.popleft()
    a, b = abs(x-ex), abs(y-ey)
    dis = math.sqrt((a*a)+(b*b))
    if dis <= mdis:
        mdis = dis
        res = (x, y)
    else:
        break
    xx, yy = px+x, py+y
    Q.append((xx, yy))
print(res[0], res[1])
