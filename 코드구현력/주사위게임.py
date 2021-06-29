# list로 받아서 collections 진행 if문 배분

N = int(input())
res = 0
for n in range(N):
    m = input().split()
    m.sort()
    a,b,c = map(int, m)
    if a == b and b == c:
        price = 10000 + a*1000
    elif a == b or a == c:
        price = 1000 +  a* 100
    elif b == c:
        price = 1000 + b * 100
    else:
        price = a*100
    if price > res:
        res = price
print(res)




"""
import collections
N = int(input())
p_list = list()
for n in range(N):
    n_list = list(map(int, input().split()))
    counters = collections.Counter(n_list)
    max = counters.most_common(1)
    if max[0][1] == 3:
        price =  10000+ max[0][0]*1000
    elif max[0][1] == 2:
        price = 1000 + max[0][0]*100
    else:
        ll = sorted(counters.items(), reverse=True)
        price = ll[0][0]*100
    p_list.append(price)
p_list.sort(reverse=True)
print(p_list[0])

"""





