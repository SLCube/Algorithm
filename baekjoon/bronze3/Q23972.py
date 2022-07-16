import sys

input = sys.stdin.readline

K, N = map(int, input().split())

X = 0

if N == 1:
    print(-1)
else:
    X = K * N // (N - 1)
    if (K * N) % (N - 1): X += 1
    print(X)
