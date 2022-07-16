import sys

input = sys.stdin.readline

board = []

for _ in range(7):
    N = int(input())

    if N % 2 != 0:
        board.append(N)

if len(board) == 0:
    print(-1)
else:
    print(sum(board))
    print(min(board))