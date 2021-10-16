import math


def GCD(a, b):
    if a%b == 0:
        return b
    return GCD(b, a%b)



ex, ey = map(int, input().split())
sx, sy, dx, dy = map(int, input().split())
if dx == 0:
    dy = 1
elif dy == 0:
    dx = 1
else:
    su = int(GCD(dx, dy))
    dx, dy = dx//su, dy//su

dis = 2147000000
res = ()
while True:
    d = math.sqrt((ex-sx)**2+(ey-sy)**2)
    if d < dis:
        res = (sx, sy)
        dis = d
    else:
        break
    sx += dx
    sy += dy
print(res[0], res[1])
