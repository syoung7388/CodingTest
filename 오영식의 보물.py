N, M = map(int, input().split())
A = []
B = []
C = []
disk = input()
for i in range(N-1, -1, -1):
    if disk[i] == 'A':
        A.append(i)
    elif disk[i] == 'B':
        B.append(i)
    else:
        C.append(i)



