
#서로 다른 N개의 합 = S // N의 최댓값 ?

n = 1
M = int(input())
while n*(n+1)/2 <= M:
    n+=1
print(n-1)
