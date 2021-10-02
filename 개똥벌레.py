import sys
input = sys.stdin.readline
N, H = map(int, input().split())
ch1 = [0]*(H+1)
ch2 = [0]*(H)
for i in range(N):
    h = int(input())
    if i%2 == 0:
        ch1[H-h] += 1
        ch1[H] -= 1
    else:
        ch2[h] -= 1
        ch2[0] += 1


for i in range(1, H):
    ch1[i] += ch1[i-1]
    ch2[i] += ch2[i-1]
    
   # ch1[i] = ch1[i]+ch2[i]

for j in range(H):
    ch2[j] += ch1[j]
M = min(ch2)
print(M, ch2.count(M))

