import sys

input = sys.stdin.readline

def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 2

    if cache.get(n):
        return cache.get(n)


    s = 1

    for i in range(2, n+1, 2):
        print(i)
        s+= f(i//2)
    cache[n] = s
    print(cache)
    return s
cache={}

for _ in range(int(input())):
    n = int(input())
    print(f(n))
    print("=============")
        
