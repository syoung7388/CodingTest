#가방에 보석 주어담기 # 17g 아래 최대 가치

n , m = map(int, input().split())

dy = [0]*(m+1) # 0~최대 그램수까지

for i in range(n):
    w, v = map(int, input().split())
    for j in range(w , m+1):
        dy[j] = max(dy[j-w]+v, dy[j])
print(dy[m])
    
