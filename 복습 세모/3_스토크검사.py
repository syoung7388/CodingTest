#스토쿠 검사

#행 검사 , 열 검사

import sys
gra = [list(map(int, input().split())) for _ in range(9)]

for i in range(9):

    hang = set()
    yul = set()
    for j in range(9):

        hang.add(gra[i][j])
        yul.add(gra[j][i])
    if len(hang) != 9 or len(yul) != 9:
        print("NO")
        sys.exit(0)


for a in range(3):
    for c in range(3):
        h = set()
        for b in range(3):
            for d in range(3):
                h.add(gra[a*3+b][c*3+d])
        if len(h) != 9:
            print("NO")
            sys.exit(0)
print("YES")        






