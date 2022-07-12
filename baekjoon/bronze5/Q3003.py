chess = [1, 1, 2, 2, 2, 8]

c = list(map(int, input().split()))

for i in range(chess.__len__()):
    print(chess[i] - c[i], end=' ')