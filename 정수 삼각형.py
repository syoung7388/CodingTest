def solution(T):
    N, M = len(T), len(T[-1])
    dy = [[0]*(M) for _ in range(N)]

    dy[0][0] = T[0][0]

    for i in range(N-1):
        for j in range(M):
            if dy[i][j] == 0: continue
            dy[i+1][j] = max(dy[i][j]+ T[i+1][j], dy[i+1][j])
            dy[i+1][j+1] = max(dy[i][j]+T[i+1][j+1], dy[i+1][j+1])


    return max(dy[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
