N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(reverse = True)

res = 0
for i in range(N):
    y, x1, x2 = arr[i][0], arr[i][1], arr[i][2]
    right = True
    left = True
    for j in range(i+1, N):
        if y == arr[j][0]: continue
        if right and arr[j][1]<=x1<arr[j][2]:
            right = False
            res += y - arr[j][0]
        if left and arr[j][1] <=x2-1<arr[j][2]:
            left = False
            res += y-arr[j][0]
    if left:
        res += y
    if right:
        res += y
print(res)
