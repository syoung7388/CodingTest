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



