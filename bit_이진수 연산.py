import sys
sys.stdin.readline
a, b = int(input(), 2), int(input(),2)

n = 10
mask = 2**n -1


print(f'{a&b:0{n}b}')

print(f'{a|b:0{n}b}')
print(f'{a^b:0{n}b}')
print(f'{mask-a:0{n}b}')
print(f'{mask-b:0{n}b}')







"""

A = list(map(int, input()))
B = list(map(int, input()))

N= 10
#A & B
for i in range(N):
    if A[i] == 1 and B[i]==1:
        print(1, end="")
    else:
        print(0, end="")
print()


#A|B
for i in range(N):
    if A[i] == 1 or B[i]==1:
        print(1, end="")
    else:
        print(0, end="")
print()

#XOR연산
for i in range(N):
    if A[i] != B[i]:
        print(1, end="")
    else:
        print(0, end="")
print()

res1 = ""
res2 = ""
for i in range(N):
    if A[i] == 1:
        res1 += "0"
    else:
        res1+= "1"
    if B[i] == 1:
        res2 += "0"
    else:
        res2 += "1"
print(res1)
print(res2)
        
"""
