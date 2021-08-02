N = int(input())+1
print(N)
dy = [0]*(N+1)

dy[1] = 1
dy[2] = 2

for i in range(3, N+1):
    dy[i] = dy[i-2]+dy[i-1]
print(dy)
print(dy[N])
