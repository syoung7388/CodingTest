N, r, c = map(int, input().split())

pos = (0, 0)
v = 0


while True:

    
    if pos == (r, c):
        print(v)
        break
    plusx = 2**(N-1)
    plusv = plusx*plusx
    
    
    if pos[0]+plusx <= r and pos[1]+plusx<=c:
        pos = (pos[0]+plusx, pos[1]+plusx)
        v += plusv*3
    elif pos[0]+plusx <= r:
        pos = (pos[0]+plusx, pos[1])
        v += plusv*2
    elif pos[1]+plusx <= c:
        pos = (pos[0], pos[1]+plusx)
        v += plus
    N -= 1
    
