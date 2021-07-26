
import sys

sto = [list(map(int, input().split())) for _ in range(9)]
for i in range(9):
    hang = set()
    yul = set()
    for j in range(9):
        hang.add(sto[i][j])
        yul.add(sto[j][i])  
    if len(hang) != 9 or len(yul) != 9:
        print("NO")
        sys.exit(0)


for a in range(3):
    for c in range(3):
        sum = 0
        for b in range(3):
            for d in range(3):
                sum += sto[a*3+b][c*3+d] 
        if sum != 45:
            print("NO")
            sys.exit(0)

    
print("YES")


    
        
