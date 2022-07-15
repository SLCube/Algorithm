import sys

input = sys.stdin.readline

N, K = map(int, input().split())
R = []

for i in range(1, N + 1):
    if N % i == 0:
        R.append(i)

R.sort()

if len(R) < K:
    print(0)
else:
    print(R[K-1])

