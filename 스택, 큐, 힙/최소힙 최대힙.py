#최소힙 최대힙


import heapq



h = []

while True:
    n = int(input())

    """
    if n == -1:
        break

    if n == 0:
        print(heapq.heappop(h))
    else:
        heapq.heappush(h,n)
    """



    if n == -1:
        break
    if n==0:
        print(-heapq.heappop(h))
    else:
        heapq.heappush(h, -n)





