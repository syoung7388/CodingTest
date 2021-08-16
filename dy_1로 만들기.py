import sys
N = int(input())

dy = [0]*(N+1)

for j in range(2, N+1):
    dy[j] = dy[j-1]+1
    if j % 2 == 0 and dy[j] >dy[j//2]+1: 
        dy[j] =dy[j//2]+1
    if j % 3 == 0 and dy[j] > dy[j//3]+1:
        dy[j] =dy[j//3]+1


print(dy[N])
