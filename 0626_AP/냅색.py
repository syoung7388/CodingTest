n , m = map(int, input().split())


dy = [0]*(m+1)


for i in range(n):
    ps, pt = map(int, input().split())
    for j in range(m, pt-1 , -1):
        dy[j] = max(dy[j-pt]+ps, dy[j])
        

print(dy[m])
