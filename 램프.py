N, M = map(int, input().split())
bit = []
ANS = 0
string = ''

for i in range(N):
    string = input()
    bit.append(string)
print(bit)
K = int(input())

for i in range(K, -1, -2):
    lst = []
    for j in range(N):
        if i == bit[j].count('0'):
            lst.append(bit[j])
    if len(lst) != 0 :
        print(lst)
        for s in lst:
            print(lst.count(s), end = "")
        ANS = max(ANS, max([lst.count(s) for s in lst]))
print(ANS)
