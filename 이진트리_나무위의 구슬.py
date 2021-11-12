
import sys
input = sys.stdin.readline
N = int(input())

tree = [[-1]*2 for _ in range(N+1)]

for i in range(1, N+1):
    left, right = map(int, input().split())
    tree[i][0] = left
    tree[i][1] = right

K = int(input())
now = 1

while K >= 0:
    lt_or_rt = K%2

    if tree[now][0] != -1 and tree[now][1] != -1:
        #홀수면 왼쪽 | 짝수면 오른쪽
        if lt_or_rt:
            now = tree[now][0]
        else:
            now = tree[now][1]
        K = K//2 + lt_or_rt 
    else:
        if tree[now][0] == -1 and tree[now][1] == -1:
            break
        elif tree[now][1] == -1:
            now = tree[now][0]
        else:
            now = tree[now][1]
print(now)
    
