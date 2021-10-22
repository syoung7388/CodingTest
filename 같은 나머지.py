def GCD(a, b):
    if a%b == 0:
        return b
    return GCD(b, a%b)


N = int(input())

arr= list(map(int, input().split()))

arr.sort()
arr = set(arr)
arr = list(arr)

for i in range(len(arr)-1):
    arr[i] = arr[i+1] - arr[i]
arr.pop()

arr.sort()
number = arr[0]
for i in range(len(arr)-1):
    if arr[i] == 0: continue
    number = GCD(arr[i], number)
print(abs(number))
