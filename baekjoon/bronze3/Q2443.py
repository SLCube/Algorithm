import sys

input = sys.stdin.readline

N = int(input())

for i in range(N):
    for j in range(i):
        print(' ', end='')
    for j in range(2 * N - (2 * i) - 1):
        print('*', end='')
    print()