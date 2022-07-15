import sys

input = sys.stdin.readline

B = [1, 0, 0]
N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    B[x-1], B[y-1] = B[y-1], B[x-1]
print(B.index(1) + 1)