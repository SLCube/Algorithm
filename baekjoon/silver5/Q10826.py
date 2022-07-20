import sys

input = sys.stdin.readline

a, b = 0, 1

N = int(input())

for _ in range(N):
    a, b = b, a + b

print(a)