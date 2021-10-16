

#defaultdict 이용 180ms

from collections import defaultdict
import sys
N = int(input())
dic = defaultdict(lambda: defaultdict(int))
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) > 1:
        first_key = word[0]+word[-1]
    else:
        first_key = word[0]
    if len(word) > 2:
        second_key = ''.join(sorted(word[1:-1]))
    else:
        second_key = ''
    dic[first_key][second_key] += 1

M = int(input())
for _ in range(M):
    arr = sys.stdin.readline().rstrip().split() #문장
    print(arr)
    res = 1
    for W in arr:
        cnt = 0
        if len(W) > 1:
            first = W[0]+W[-1]
        else:
            first = W[0]
        if len(W) > 2:
            second = ''.join(sorted(W[1:-1]))
        else:
            second = ""
        res *= dic[first][second]
    print(res)
        









""" pypy3 : 2352 ms



import sys

def check(W):
    for w in W:
        o = ord(w)
        if o <= 90:
            if ch[o-65] == 0:
                return False
            ch[o-65] -= 1
        elif o>=97:
            if ch[o-71] == 0:
                return False
            ch[o-71] -= 1
    return True        

N = int(input()) #단어의 개수
words = [sys.stdin.readline().rstrip() for _ in range(N)]
che = [[0]*54 for _ in range(N)]
for i in range(N):
    for w in words[i]:
        o = ord(w)
        if o <= 90:
            che[i][o-65] += 1
        elif o >= 97:
            che[i][o-71] += 1

M = int(input()) #문장의 개수
for _ in range(M):
    arr = list(map(str, sys.stdin.readline().rstrip().split())) #문장
    res = 1
    for W in arr: #문장안의 단어들
        cnt  = 0      
        for i in range(N):
            ch = che[i][:]
            if words[i][0] != W[0] or words[i][-1] != W[-1] or len(words[i]) != len(W): continue
            if check(W):
                cnt += 1
        res *= cnt
    print(res)

"""
