


def DFS(L):
    global aws
    if L == N:
        
        cha = max(am) - min(am)
        if cha < aws:
            tmp = set()
            for a in am:
                tmp.add(a)
            if len(tmp) == 3:
                aws = cha
            
        
        
        return

    else:
        for i in range(3):
            am[i] += C[L]
            DFS(L+1)
            am[i] -= C[L]




if __name__ == "__main__":
    N = int(input())
    C = list(map(int, input().split()))

    am = [0]*3
    aws = 2147000000
    DFS(0)
    print(aws)
