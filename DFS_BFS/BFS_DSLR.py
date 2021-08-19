from collections import deque
import sys
input = sys.stdin.readline


if __name__== "__main__":
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())
        Q = deque([(A, "")])
        ch = [0]*(100000)
        ch[A] = 1
        while Q:
            x, order = Q.popleft()
            if x == B:
                print(order)
                break
            if x*2 <= 9999 and ch[x*2] == 0:
                ch[x*2] = 1
                Q.append((x*2,order+'D' ))
            if x*2 >9999 and ch[(x*2)%10000] == 0:
                ch[(x*2)%10000] = 1
                Q.append(((x*2)%10000, order+'D'))
            if x-1 < 0 and ch[9999] == 0:
                ch[9999]= 1
                Q.append((9999, order+'S'))
            if x-1 >= 0 and ch[x-1] == 0:
                ch[x-1] = 1
                Q.append((x-1, order+'S'))
            nx = int((x%1000)*10+x/1000)
            if ch[nx] == 0:
                ch[nx] = 1
                Q.append((nx, order+'L'))
            nx = int((x%10)*1000+x/10)
            if ch[nx] == 0:
                ch[nx] = 1
                Q.append((nx, order+'R'))
                

                
