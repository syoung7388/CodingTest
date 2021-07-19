from collections import deque


if __name__ == "__main__":
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    w.sort()
    Q = deque(w)
    cnt = 0

    while Q:

        if len(Q) == 1:
            cnt += 1
            break
        if Q[0]+Q[-1] > M:
            cnt += 1
            Q.pop()
        else:
            cnt += 1
            Q.pop()
            Q.popleft()
            
            



    

    """
    ch = [0]*N
    for i in range(N):
        if ch[i] == 0:
            ma = M - w[i]
            cnt += 1
            ch[i] = 1
            for j in range(N-1, i, -1):
                if ch[j]== 0 and w[j] <= ma:
                    ch[j]=1
                    break
    """
    print(cnt)
    
    
    
