N, r, c = map(int, input().split())

lo = (0,0)
v= 0

while True:

    if lo == (r,c):
        print(v)
        break

    xy = 2**(N-1)

    plus =xy*xy

    if r >= lo[0]+xy and c >= lo[1]+xy: #4사분면
        lo = (lo[0]+xy, lo[1]+xy)
        v = v + plus*3
    elif r >= lo[0]+xy:
        lo = (lo[0]+xy, lo[1])
        v = v + plus*2
    elif c >= lo[1]+xy:
        lo = (lo[0], lo[1]+xy)
        v = v + plus

    N -= 1
        
