

from collections import deque
if __name__ == "__main__":
    N = int(input())
    p = dict()

    for i in range(N):
        word = input()
        p[word] = 1
    for j in range(N-1):
        word2 = input()
        p[word2] = 0
    for k,v  in p.items():
        if v == 1:
            print(k)
            

    






    """ 간단쓰 방법
    s1 = set(input() for _ in range(N))
    s2 = set(input() for _ in range(N-1))
    res = s1-s2
    for x in res:
        print(x)
    """

    
