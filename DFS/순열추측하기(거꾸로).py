
import sys
def DFS(L, sum):
    if L == n and sum == f:
        for x in p:
            print(x, end = " ")
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                p[L] = i
                DFS(L+1, sum+(p[L]*b[L]))
                ch[i]=0
          
if __name__ == "__main__":
    n, f = map(int, input().split())
    p = [0]*n #-> 조합한 숫자 
    b = [1]*n #-> nCr값 입력
    ch = [0]*(n+1) #-> 선정한 숫자 체크
    for i in range(1, n): #첫 수 , 막 수 는 일정값임
        b[i] = b[i-1]*(n-i) // i
    DFS(0, 0)
    


