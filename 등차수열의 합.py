


def f(x):
    n = (x-a)/d[K] + 1
    return n

left = int(input())
right = int(input())
K = int(input())

l = left

fir = {2:3, 3:6, 4:14, 5:10}
d = {2:1, 3:3, 4:2, 5:5}

res = 0
a = 0

if left <= fir[K]:
    left = fir[K]
    
while True:
    num = f(left)
    if num == int(num):
        a = left
        break
    left += 1
    
while True:
    num = f(right)
    if num == int(num):
        res = int(num)
        break
    else:
        right -= 1
if K == 4 and l <= 10: #10 추가 시켜주기
    res += 1


print(res)
