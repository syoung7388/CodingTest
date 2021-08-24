for i in range(10):
    print(i, '→', bin(i))
#원소 추가
n = 2
print(bin(0b0010|(1<<n)))

#원소 제거
n = 3
print(bin(1<<n))
print(bin(~(1<<n)))
print(bin(0b1010 & ~(1<<n)))
