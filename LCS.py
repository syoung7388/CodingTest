N = int(input())
nums = list(map(int, input().split()))

dy = [[0 for _ in range(21)] for _ in range(N-1)]



dy[0][nums[0]] = 1
for i in range(1, N-1):
    for j in range(21):
        if dy[i-1][j] == 0: continue

        prev = j
        next = nums[i]

        if 0<=prev+next<=20:
            dy[i][prev+next] += dy[i-1][prev]
        if 0<=prev-next<=20:
            dy[i][prev-next] += dy[i-1][prev]

print(dy[N-2][nums[-1]])
