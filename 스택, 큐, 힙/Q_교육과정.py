
from collections import deque

if __name__ == "__main__":

    need = input()
    N = int(input())
    for i in range(N):
        plan = input()
        dQ = deque(need)
        for x in plan:
            if x in dQ:
                if x != dQ.popleft():
                    print('#%d NO' %(i+1))
                    break
        else:
            if len(dQ) == 0:
                print('#%d YES' %(i+1))
            else:
                print('#%d NO' %(i+1))
                
