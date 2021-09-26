import math
def prm(n):
    
    ch = [0]*(n+1)
    ch[0] = 1
    ch[1] = 1
    p = []
    for i in range(2, n+1):
        if ch[i] == 0:
            p.append(i)
            for j in range(i+i, n+1 , i):
                ch[j] = 1
    return p




A, B = map(int, input().split())

p = prm(int(B**0.5)) #31**2 = 1000

cnt = 0

for n in p:
    k = n
    while k <= B:
        k = k*n
        cnt += (A<=k<=B)
print(cnt)        



















"""
N = 10**7 +5
ch = [1]*(N+100)
ch[0] = 0
ch[1] = 0

prime = 2

while prime*prime <= N:
    if not ch[prime]:
        prime += 1
        continue
    print(prime)
    for t in range(2*prime, N+3, prime):
        ch[t] = 0
    prime += 1

"""




"""

ch = [0]*(B+1)
ch[1] = 1
S = 0
for i in range(2, B+1):
    if ch[i] == 0:
        z = i**2
        cnt = 0
        for j in range(i+i, B, i):
            if j == z and A <= z <=B:
                cnt += 1
                z *= i
            if j > z:
                break
            ch[j] = 1
        if cnt == 0:
            break
        S += cnt
print(S)


def getCnt(n):
    cnt = 0
    for i in range(2, B//2+1):
        if n**i > B:
            break
        if A<= n**i <= B:
            cnt += 1
    return cnt
"""
