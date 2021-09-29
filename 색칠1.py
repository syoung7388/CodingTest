w,h, f, c, x1, y1, x2, y2 = map(int, input().split())
total = w*h

paint = (x2-x1)*(y2-y1)*(c+1)
#1) 왼쪽크기 <= 오른쪽크기
if f <= w/2:
    
    if f <= x1: #색칠 범위가 포함 X
        total -= paint
    else: #색칠 범위 포함 O
        total -= (paint + (min(f, x2)-x1)*(y2-y1)*(c+1))
#2) 왼쪽크기 < 오른쪽 크기
else: 
    if w <= x1+f: #색칠범위 포함 X
        total -= paint
    else: #색칠범위 포함 O
        total -= (paint+ (min(w,f+x2) - (f+x1)*(y2-y1)*(c+1)))
print(total)        
    












"""
[틀린 답]
total = N*M
#total - 색칠한 부분
#N 부분 (y축 겹치는 부분)
if c != 0:
    overlap = N//c + N%c
else:
    overlap = 1
    
y_paint = (x2-x1)*(y2-y1)
total -= overlap*y_paint



#x 축 겹치는 부분

# f = 4, M= 5 -> 겹쳐지는 부분 [3], 4 한개
# M//f 



if 0 < f < M:
    s, e= x1 +f, x2-1+f #3, 4
    x_paint = 0
    over = min(M-f, f)
    for i in range(f-over, f):
        if s <= i+f <= e and 0<=i+f < M:
            x_paint += 1
        
    total -= x_paint*(overlap)


print(total)
"""
