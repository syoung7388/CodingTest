#import sys
#sys.stdin = open("input.txt","rt")

#N의 약수 구하기
#sort -
#K번째로 작은 수 구하기 (K =< N)
#존재 X -> -1
N, K = map(int, input().split())
"""
count = 0
for i in range(1, N+1):
    if N%i == 0:
        count += 1
    if count == K:
        answer = i
        break
else:
    answer = -1
print(answer)
"""

Y = list()
for num in range(1, N+1):
    if N % num == 0:
        Y.append(num)
Y.sort()
#print(Y)
if len(Y) >= K:
    answer = Y[K-1]
else:
    answer = -1
print(answer)








