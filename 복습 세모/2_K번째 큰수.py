#K번째 큰수


if __name__ == "__main__":
    N, K = map(int, input().split())
    cards = list(map(int, input().split()))
    cards.sort
    res = set()

    for i in range(N):
        for j in range(i+1, N):
            for l in range(j+1, N):
                res.add(cards[i]+cards[j]+cards[l])
    R = list(res)
    R.sort(reverse=True)
    print(R[K-1])

    
    
    
