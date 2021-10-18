M = int(input())
S = input()
N = len(S)
res = 2147000000
for p in range(1, M+1):
    cnt = 0
    for i in range(p):
        dic = {'A':0, 'C':0, 'G':0, 'T':0}
        for j in range(i, N, p):
            dic[S[j]] += 1
        cnt += (sum(dic.values()) - max(dic.values()))
    res = min(cnt, res)
        
    
    
print(res)
