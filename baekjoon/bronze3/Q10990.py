import sys

input = sys.stdin.readline

N = int(input())

for i in range(1, N+1):
    print(" " * (N - i), end='')
    for j in range(2 * i - 1):
        if j == 0 or j == (2 * i - 2):
            print("*", end='')
        else:
            print(" ", end='')
    print()