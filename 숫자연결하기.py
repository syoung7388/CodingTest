N , K = map(int, input().split())

bf = N%K
if bf == 0:
    print(1)
    sys.exit(0)
    
ch = [0]*(K+1)
res = -1
for i in range(2, K+1):
    S = int(str(bf)+str(N))
    if S%K == 0:
        res = i
        break
    if ch[S%K] == 1:
        break
    ch[S%K] = 1
    bf = S%K
print(res)



"""
import sys

N, K = map(int, input().split())
dic = dict()
bf = N%K
if bf == 0:
    print(0)
    sys.exit(0)
res = -1
cnt = 1
while True:
    S = int(str(bf)+str(N))
    cnt += 1
    if S%K == 0:
        res = cnt
        break
    if S%K in dic:
        break
    dic[S%K] = 1
    bf = S%K
print(res)

for k in range(1, 100):
    print(k,":", int(str(1000999)*k)%99999)

for k in range(1, 10):
    for n in range(1, 10):
        print( "n:", n, "k:", k)
        for i in range(1,10):
            s = int(str(n)*i)
            print(i,":",s%k)

            
"""
