import sys
input = sys.stdin.readline

N = int(input())
if N == 1:
    print(1)
    sys.exit(0)

ch = []
arr = list(map(int, input().split()))
ch = [arr[0],arr[1],arr[2]]
res = 1
for _ in range(1, N):
    arr = list(map(int, input().split()))
    if not arr[0] in ch and not arr[1] in ch and not arr[2] in ch:
        ch.clear()
        res += 1
    ch.append(arr[0])
    ch.append(arr[1])
    ch.append(arr[2])

print(res)
