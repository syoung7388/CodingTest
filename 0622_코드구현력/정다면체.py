# N ,M
# N,M list로 만들기
#for문 돌려서 합구하기
#개수 구하기
N, M = map(int, input().split())
"""
import collections
sum = list()
for i in range(1,N+1):
    for j in range(1, M+1):
        sum.append(i+j)

counter = collections.Counter(sum)
m = counter.most_common(1)
max = m[0][1]
answer= []
for num in counter.most_common():
    if max == num[1]:
        answer.append(num[0])
for i in answer:
    print(i, end=" ")
"""
cnt = [0]*(N+M+3)
max = -2147000000
for i in range(1, N+1):
    for j in range(1, M+1):
        cnt[i+j]+=1
for i in range(N+M+1):
    if cnt[i] > max:
        max = cnt[i]
for i in range(N+M+1):
    if cnt[i] == max:
        print(i, end=" ")








