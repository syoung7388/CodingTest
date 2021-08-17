for _ in range(int(input())):
    N = int(input())
    dy = [0]*(N+1)
    for i in range(N+1):
        if i == 0 or i == 1:
            dy[i] = 0
        else:
            dy[i] = dy[i-2]+2
    print(dy)
