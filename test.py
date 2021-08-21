
import sys

def getHim(x, y):
    if x == 0: return 2
    elif x == y: return 1
    elif abs(x-y)%2 == 0: return 4
    else: return 3
order = list(map(int, input().split()))
N = len(order)
Max = sys.maxsize
dy = [[[Max]*5 for _ in range(5)] for _ in range(N)]
dy[0][0][0] = 0

for i in range(N-1):
    for l in range(5):
        for r in range(5):
            if dy[i][l][r] != Max:
                dy[i+1][l][order[i]] = min(dy[i][l][r]+getHim(r, order[i]), dy[i+1][l][order[i]])
                dy[i+1][order[i]][r] = min(dy[i][l][r] + getHim(l, order[i]), dy[i+1][order[i]][r])



res = Max
for d in dy[-1]:
    res = min(res, min(d))
print(res)

"""
for d in dy:
    for di in d:
        print("[" ,  end=" ")
        for r in di:
            if r == Max:
                print("M", end=" ")
            else:
                print(r, end=" ")
        print("]", end =" ,")
    print()
"""
