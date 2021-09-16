import sys
K= int(input())

P = []

for _ in range(K):
    P.append([x for x in range(10)])

gra = []

for _ in range(5):
    gra.append(input())


I = [
	[[1], 								[1, 4], 												[]		],
	[[1, 2, 3, 7], 				[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [5, 6]],
	[[1, 7],							[0, 1, 7],											[]		],
	[[1, 3, 4, 5, 7, 9],	[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [2]		],
	[[1, 4, 7], 					[1, 4, 7], 											[]		]
]


print(P)
for i in range(4*K-1):
    for j in range(5):
        if gra[j][i] == '#':
            P[i//4] = list(filter(lambda x : x not in I[j][i%4], P[i//4]))
    if not P[i//4]:
        print(-1)
        break
else:
    print(P)
    
    cnt = 1
    for i in range(K):
        cnt *= len(P[i])

    S = 0
    for i in range(K):
        S *= 10
        S += sum(P[i])*(cnt/len(P[i]))
    print(S/ cnt)
    

