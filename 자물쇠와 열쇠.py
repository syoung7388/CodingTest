



def mathch(arr, key, rot, r, c):
    N = len(key)
    for i in range(N):
        for j in range(N):
            if rot == 0: #그대로
                arr[r+i][c+j] += key[i][j]
            elif rot == 1: #왼쪽으로 90도 회전
                arr[r+i][c+j] += key[N-1-j][i]
            elif rot == 2: #180도 회전
                arr[r+i][c+j] += key[N-1-i][N-1-j]
            else: #오른쪽으로 90도 회전
                arr[r+i][c+j] += key[j][N-1-i]
def check(arr, offset, n):
    for i in range(n):
        for j in range(n):
            if arr[offset+i][offset+j] != 1:
                return False
    return True
def solution(key, lock):

    offset = len(key)-1 #2
    for r in range(offset+len(lock)): #0~4
        for c in range(offset+len(lock)): # → key 복붙 시작점
            for rot in range(4): # → 회전값 
                arr = [[0 for _ in range(58)] for _ in range(58)]

                #자물쇠 복붙
                for i in range(len(lock)):
                    for j in range(len(lock)):
                        arr[offset+i][offset+j] = lock[i][j]

                #key랑 자물쇠(arr) 매치 시켜보기 | 회전값은 rot로
                mathch(arr, key, rot, r, c)

                #전부 1인지 체크하는 함수
                if check(arr, offset, len(lock)):
                    return True
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
