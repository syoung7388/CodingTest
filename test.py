N,K = map(int, input().split())
res = 0
while bin(N).count('1') > K:
    p = 2**bin(N)[::-1].index('1')
    res += p
    N += p
print(res)
