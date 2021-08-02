import sys


def DFS(num, digit):
    if digit > 10:
        return
    
    res.append(num)
    for j in range(10):
        if num%10 > j:
            DFS(num*10+j, digit+1)


if __name__=="__main__":

    N = int(input())
    if N >= 1023:
        print(-1)
        sys.exit(0)
    
    res = list()
    for i in range(10):
        DFS(i, 1)
    res.sort()
    print(res[N])




  
