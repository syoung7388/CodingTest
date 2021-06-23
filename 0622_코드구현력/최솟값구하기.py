arr = [3, 5, 6, 2, 1]
brr = arr[0]
for i in arr:
    if i < brr:
        brr = i
print(brr)