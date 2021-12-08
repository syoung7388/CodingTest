

G = [{0.05:[(0, -2)], 0.1:[(-1, -1), (1, -1)], 0.07:[(-1, 0), (1, 0)], 0.01:[(-1, 1), (1, 1)], 0.02:[(-2, 0), (2, 0)]}]



for _ in range(3):

    g = {}

    for k, v in G[-1].items():

        arr = []

        for x, y in v:
            arr.append((-y, x))
        g[k] = arr
    G.append(g)
print(G)

