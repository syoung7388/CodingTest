N= int(input())
nums = list(map(int, input().split()))
def reverse(n):
    return int(str(n)[::-1])
"""
def reverse(n):
    res = 0
    while n > 0:
        t= n % 10 #나머지
        res = res * 10 + t 
        n = n // 10 #몫         

"""


def isPrime(r_n):
    if r_n == 1:
        return False
    for i in range(2, r_n//2+1): #소수는 반밖에 존재 안함
        if r_n%i == 0:
            return False

for n in nums:
    r_n = reverse(n)
    if isPrime(r_n) != False:
        print(r_n,  end=" ")


"""
27
469 84 8851 189 69 1210 682 57 6217 484 8 3590 662 36 8275 887 17 1254 462 67 8969 141 70 5603 958 100 3843 


"""