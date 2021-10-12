

Max = int(input()) #맥스레벨
avatar = list(map(int, input().split())) #레벨별 캐릭터 수
him = list(map(int,  input().split())) #캐릭터별 수
D = int(input())
N = len(avatar)
S = 0

            
dp  = [[-1]*(N) for _ in range(D+1)]

for i in range(N):
    S += avatar[i]*him[i]


for d in dp:
    print(d)
