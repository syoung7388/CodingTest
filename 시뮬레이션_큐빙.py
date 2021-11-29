import sys
input = sys.stdin.readline

"""
0    1   2
rrr bbb ccc
rrr bbb ccc
rrr bbb ccc

bf = rrr
1 = bf
bf = bbb

2 = bf
bf = ccc

3 = 0
bf 



"""




def cmd(n, c):
    if n == 'L':
        if c == '+':
            return [0, 4, 5, 1, 0]
        if c == '-':
            return [0, 1, 5, 4, 0]  
    elif n == 'R':
        if c == '+':
            return [0, 1, 5, 4, 0]  
        if c == '-':
            return [0, 4, 5, 1, 0]     
    elif n == 'D':
        if c == '+':
            return [1, 2, 4, 3, 1]
        if c == '-':
            return [1, 3, 4, 2, 1]
    elif n == 'U':
        if c == '+':
            return [1, 3, 4, 2, 1]
        if c == '-':
            return [1, 2, 4, 3, 1]
    elif n == 'B':
        if c == '+':
            return [0, 2, 5, 3, 0] 
        if c == '-':
            return [0, 3, 5, 2, 0]
    elif n == 'F':
        if c == '+':
            return [0, 3, 5, 2, 0]
        if c == '-':
            return [0, 2, 5, 3, 0]

        
def sero_Turn(T, n, b):
    bf = (gra[T[0]][0][n], gra[T[0]][1][n], gra[T[0]][2][n])
    print(n, b)
    for i in range(1, 5):
        temp = (gra[T[i]][0][n], gra[T[i]][1][n], gra[T[i]][2][n])
        if (n == 0 and b == '+') or (n == 2 and b == '-'):
            if i%2 == 0:
                gra[T[i]][2][n], gra[T[i]][1][n], gra[T[i]][0][n] = bf
            else:
                gra[T[i]][0][n], gra[T[i]][1][n], gra[T[i]][2][n] = bf
        elif  (n == 2 and b == '+') or (n == 0 and b == '-'):
            if i%2 == 0:
                gra[T[i]][0][n], gra[T[i]][1][n], gra[T[i]][2][n] = bf
            else:
                gra[T[i]][2][n], gra[T[i]][1][n], gra[T[i]][0][n] = bf

        bf = temp
    

def garo_Turn(T, n):
    bf = gra[T[0]][n][:]
    for i in range(1, 5):
        #print(T[i])
        #print("bf:", bf, "n:", n)
        temp = gra[T[i]][n][:]
        gra[T[i]][n] = bf
        bf = temp

        
        
    
    
    
dic = {'U':0, 'B':0, 'L':0, 'R':2, 'F':2, 'D':2}        

for _ in range(int(input())):        
    N = int(input())
    gra = []
    for color in ['w','o', 'g', 'b', 'r', 'y']:
        gra.append([[color]*3 for _ in range(3)])
    
    arr = list(map(str, input().split())) 
    
    for a in arr:
        print(a, "----------------")
        nums = cmd(a[0], a[1])
        if a[0] == 'L' or a[0] == 'R':
            sero_Turn(nums, dic[a[0]], a[1])
        else:
            garo_Turn(nums, dic[a[0]])

    for g in gra:
        for a in g:
            print(a)
        print()
    print()


            
    for i in range(3):
        for j in range(3):
            print(gra[0][i][j], end = "")
        print()
    print()
