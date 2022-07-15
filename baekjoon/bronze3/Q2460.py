import sys

input = sys.stdin.readline

N = [0]

for i in range(10):
    x, y = map(int, input().split())

    N.append(N[i] + y - x)

print(max(N))
