def GCD(a, b):
    if a%b == 0:
        return b
    return GCD(b, a%b)



N = input()
digit = [int(c) for c in N]
lcm = 1

for i in digit:
    if i == 0: continue
    lcm = lcm*i / GCD(lcm, i)

N = int(N)
ten = 1


while True:
    can_div = False
    for i in range(ten):
        #print(N*ten+i)
        if (N*ten+i)%lcm == 0:
            print(N*ten+i)
            can_div = True
            break
    if can_div:
        break
    ten *= 10



""" Q 방식
from collections import deque
N = input()
Q = deque([N])
M = len(N)
while Q:
    X = Q.popleft()
    arr = int(X)
    for j in range(M):
        if X[j] == '0': continue
        if arr%int(X[j]) != 0:
            break
    else:
        print(X)
        break
    for i in range(10):
        nX = X + str(i)
        Q.append(nX)
"""           
