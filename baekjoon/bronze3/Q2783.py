import sys

input = sys.stdin.readline

gimbabs = []

X1, Y1 = map(int, input().split())

N = int(input())

gimbabs.append(X1 * 1000 / Y1)

for _ in range(N):
    X, Y = map(int, input().split())

    gimbabs.append(X * 1000 / Y)

print(min(gimbabs))