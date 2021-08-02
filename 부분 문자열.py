
import sys


Str = input()
subStr = input()

Len = len(subStr)
arr = [0]*(Len)
j = 0
for i in range(1, Len):
    while j > 0 and subStr[i] != subStr[j]:
        j = arr[j-1]
    if subStr[i] == subStr[j]:
        j += 1
        arr[i] = j

idx = 0
count = 0
for l in range(0, len(Str)):
    while idx > 0 and Str[l] != subStr[idx]:
        idx = arr[idx-1]
    if Str[l] == subStr[idx]:
        if idx == Len-1:
            count += 1
            break
        else:
            idx += 1

print(count)
