import sys

def ABC(a, b, c, s, l1, l2):
    if len(s) == N:
        print(s)
        sys.exit(0)

    if dp[a][b][c][l1][l2] == 1:
        return 
    dp[a][b][c][l1][l2] = 1

        
    if a < A:
        ABC(a+1, b, c, s+"A", l2, 1)
        
    
 
    if b < B and l2 != 2:
        ABC(a, b+1, c, s+"B",l2 , 2)
        
    if c < C and l1 != 3 and l2 != 3:
        ABC(a, b, c+1, s+"C", l2, 3)
S = input()

N = len(S)
if N == 1:
    print(S)
    sys.exit(0)
A = S.count('A')
B = S.count('B')
C = S.count('C')
dp = [[[[[0]*4 for _ in range(4)] for _ in range(C+1)] for _ in range(B+1)] for _ in range(A+1)]
ABC(0, 0, 0, "", 0, 0)

print(-1)
