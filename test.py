W, H, f, c, x1, y1, x2, y2 = map(int, input().split())

tot = W*H
plus = (x2-x1)*(y2-y1)*(c+1)
tot -= plus

if f <= W//2:
    if x1 < f:
        tot -= (min(f, x2) - x1)*(y2-y1)*(c+1)
else:
    if x1+f < W:
        tot -= ( min(x2+f, W)-(x1+f))*(y2-y1)*(c+1)
print(tot)
