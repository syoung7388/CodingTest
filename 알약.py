def Mcnt(x, y, z):
    if dy[x][y] != 0:
        return dy[x][y]
    a = b = 0
    if y-1 >= 0:
        a = Mcnt(x, y-1, z)
    if x-1>=0 and y+1<=z*2:
        b = Mcnt(x-1, y+1, z)
    dy[x][y] = a+b
    return dy[x][y]

med = list()
while True:
    m = int(input())
    if m == 0:
        break
    med.append(m)
maxm = max(med)
dy = [[0 for _ in range(maxm*2+1)] for _ in range(maxm+1)]
dy[0] = [1 for _ in range(maxm*2+1)]

for i in med:
    print(Mcnt(i, 0, i))

    
