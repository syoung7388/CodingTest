h, w = map(int, input().split())

height = list(map(int, input().split()))


maxH = max(height)
maxIndex = height.index(maxH)

total= 0
temp= 0

for  i in range(maxIndex+1):
    if height[i] > temp:
        temp = height[i]
    total += temp
temp = 0
for j in range(w-1, maxIndex, -1):
    if height[j] > temp:
        temp = height[j]
    total+= temp
print(total - sum(height))





