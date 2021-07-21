

if __name__ == "__main__":
    cards = list(range(21))

    for n in range(10):
        a, b = map(int, input().split())

        size = b-a+1

        for i in range(size//2):
            cards[a+i], cards[b-i] = cards[b-i], cards[a+i]

    for c in range(1, 21):
        print(cards[c], end=" ")

        
