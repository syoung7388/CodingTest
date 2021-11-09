import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def DFS(n):
    global cnt
    cnt += 1
    for g in G[n]:
        if g == head[n]: continue
        head[g] = n
        DFS(g)
        dp[n][1] += dp[g][0] #현재 마을을 우수마을 선정 O
        dp[n][0] += max(dp[g][0], dp[g][1]) #현재마을을 우수마을로 선정 X
        

N = int(input())
C = [0]+list(map(int, input().split()))



dp = [[0, C[i]] for i in range(N+1)]

G = [[] for _ in range(N+1)]
head = [x for x in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)


cnt = 0
DFS(1)
print(max(dp[1][1], dp[1][0]))
print(cnt)

"""

[내가한 방식] - dp (Memorization) + 선택 노드확인(bit연산자)

                        1번노드
             O                           X

    2번  +  3번  +  4번              5번  +  6번
   O  X     O X     O X              O X     O X

   
[시간 복잡도]

O(N)인접그래프 만들기 + O(2N)dp 돌리기 => O(3N)
             

def U(n, flag, bit):
    if dp[n][flag] != -1:
        return dp[n][flag]
    arr = 0
    for g in G[n]:
        if bit & (1<<g) != 0: continue
        temp = U(g, False, bit|(1<<g))
        if not flag:
            temp = max(temp, U(g, True, bit|(1<<g))+p[g])
        arr += temp
    dp[n][flag] = max(dp[n][flag], arr)
    return dp[n][flag]
N= int(input())
p = list(map(int, input().split()))
p.insert(0, 0)
G = [[] for _ in range(N+1)]
for _ in range(1, N):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
G[0].append(1)
#print(G)
dp = [[-1]*2 for _ in range(N+1)]
print(U(0, False, 1<<0))


"""
