from collections import deque
import sys

N = int(input())
crain= list(map(int, input().split()))
crain.sort(reverse = True)

B = int(input())
box = list(map(int,input().split()))
box.sort(reverse= True)

res = 0
while len(box) > 0:
    res += 1
    for c in crain:
        for i in range(len(box)):
            if box[i] <= c:
                del box[i]
                break
            


print(res)
