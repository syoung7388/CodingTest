import sys
input = sys.stdin.readline
word  = input()
w = input()


for i in range(len(word)):
    if word[i] == w[0] and len(word)-i-1 >= len(w)-1:
        for wo in range(len(w)-1):
            if w[wo] != word[i+wo]:
                break
        else:
            print(1)
            break
                
else:
    print(0)
