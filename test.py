N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(reverse = True)

res = 0
for i in range(N):
    h, x1, x2 = arr[i]
    left = True
    right = True
    for j in range(i+1, N):
        if h == arr[j][0]: continue

        
        if left and arr[j][1]<= x1 < arr[j][2]:

            left = False
            res += h-arr[j][0]
        
        if right and arr[j][1] <= x2-1 <= arr[j][2]:

            right = False
            res += h-arr[j][0]
    if left:
        res += h
    if right:
        res += h
print(res)
