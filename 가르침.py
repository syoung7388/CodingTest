
import sys

n, k = map(int, input().split())

if k < 5:
    print(0)
    sys.exit(0)
elif k == 26:
    print(n)
    sys.exit(0)

answer = 0   
words = [set(sys.stdin.readline().rstrip()[4:-4]) for _ in range(n)]
learn = [0]*26

print(words)
for c in ('a', 'c', 'i', 'n', 't'):
    learn[ord(c)-ord('a')] = 1


def DFS(idx, cnt):
    global answer
    if cnt == k-5:
        readcnt = 0
        for word in words:
            for w in word:
                if not learn[ord(w)-ord('a')]:
                    break
            else:
                readcnt += 1
        answer = max(answer, readcnt)


    else:
        for i in range(idx, 26):
            if not learn[i]:
                learn[i] = 1
                DFS(i+1, cnt+1)
                learn[i] = 0
                
DFS(0,0)
print(answer)
