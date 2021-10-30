import math
import sys
input = sys.stdin.readline

"""
1) 2 ~ 마지막 가능 제곱수

2) 등차수열이랑 똑같음
   범위를 줄이기 위해서 등차수열의 항공식 이용함

3) 메모리초과를 방지하기 위해서 ch 배열을 b-a+1만 둔다 !!


"""


a, b = map(int, input().split())
N = b-a+1

ch = [0]*(N)
for i in range(2, int(b**0.5)+1): 
    z = i**2
    for j in range(math.ceil((a-z)/z + 1)*z, b+1, z):
        if ch[j-a] == 0: 
            ch[j-a] = 1
            
print(ch.count(0))
