N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort(key = lambda x : x[0], reverse = True)

res = 0
for i in range(N):
    a, a1, a2 = arr[i]
    left = False
    right = False
    for j in range(i+1, N):
        b, b1, b2 = arr[j]
        if a == b: continue
        if not left and b1 <= a1 < b2:
            left = True
            res += a-b
        if not right and b1 <= a2-1 < b2:

            right = True
            res += a-b
    if not left:
        res += a
    if not right:
        res += a
print(res)
