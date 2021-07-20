
from collections import deque


if __name__ == "__main__":

    N, K = map(int, input().split())

    dq = list(range(1, N+1))
    dq= deque(dq)
    
    while dq:
        for _ in range(K-1):
            cur = dq.popleft()
            dq.append(cur)
        dq.popleft()
        if len(dq) == 1:
            print(dq.popleft())
 


