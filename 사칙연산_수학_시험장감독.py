N = int(input())
arr = list(map(int, input().split()))
A, B = map(int, input().split())
res = 0
for a in arr:
    a -= A
    cnt = 0
    if a > 0:
        cnt = a//B + 1 if a%B else a//B
    res += (cnt+1)
print(res)
