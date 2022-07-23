import sys
import math

input = sys.stdin.readline

R, C, W = map(int, input().split())
result = 0

for i in range(1, W + 1):
    for j in range(i):
        result += math.comb(R - 2 + i, C - 1 + j)

print(result)