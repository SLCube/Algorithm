import sys
import math

input = sys.stdin.readline

N, K, M = map(int, input().split())

print(math.comb(N, K) % M)

