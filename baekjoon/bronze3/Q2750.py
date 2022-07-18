import sys

input = sys.stdin.readline

N = int(input())

board = []

for _ in range(N):
    board.append(int(input()))

board.sort()

for i in board:
    print(i)
