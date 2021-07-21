
from collections import deque


if __name__ == "__main__":

    N, M = map(int, input().split())
    dic = deque((k, v) for k, v in enumerate(list(map(int, input().split()))))
    cnt = 0
    while True:
        cur = dic.popleft()


        if any(cur[1] < x[1] for x in dic):
            dic.append(cur)
        else:
            cnt += 1
            if cur[0] == M:
                print(cnt)
                break
            
            


    
        
    
