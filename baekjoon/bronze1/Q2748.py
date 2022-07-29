import sys

input = sys.stdin.readline

a, b = 0, 1

N = int(input())

for i in range(0, N):
    a, b = b, a + b

print(a)