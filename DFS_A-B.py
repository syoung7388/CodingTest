import sys
def DFS(num, cnt):
    if num == M:
        print(cnt)
        sys.exit(0)
    if num > M:
        return
    else:
        DFS(num*2, cnt+1)
        DFS(num*10+1, cnt+1)

if __name__ == "__main__":
    N, M = map(int, input().split())
    DFS(N, 1)
