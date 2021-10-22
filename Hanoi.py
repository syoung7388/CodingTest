def hanoi(N, n_from, n_to, temp):
    if N == 1:
        #시작 -> 도착
        print(n_from , n_to)
        return

    #시작 - >  보조기둥 
    hanoi(N-1, n_from, temp, n_to)
    print(n_from, n_to)

    #보조기둥 -> 도착
    hanoi(N-1, temp, n_to, n_from)

K = int(input())
print(2**K - 1)
hanoi(K, 1, 3, 2)
