n = 0    # 숫자 1, 2, 3, ...
step = 1 # 증가/감소 크기: 1, -1
x= 0    # 줄 위치
y = -1   # 칸 위치 (배열 선두보다 한칸 앞)
size = 5 # 배열 크기 (5*5 배열)
arr = [[0]*size for i in range(size)]   # 2차원 배열 구조
 
while True:
    print(size)
    for _ in range(size):  # 몇 칸 진행할까
        n += 1
        y += step
        arr[x][y] = n


    size -= 1
    print(size)
    if size < 1:  # 출력할 게 없으면 종료
        break
    for _ in range(size):  # 몇 줄 진행할까
        n += 1
        x += step
        arr[x][y] = n       
    step = -step  # 증감 방향을 반대로



    for a in arr:
        print(a)
    print()
