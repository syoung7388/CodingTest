# N개의 숫자열
# s번째 ~ e번째 오름차순 정렬
#k번째 출력

#import sys
#sys.stdin = open("input.txt","rt")
T = int(input())
for t in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s-1: e]
    a.sort()
    print("#%d %d"%(t+1,a[k-1]))



