import sys

input = sys.stdin.readline

board = []

for _ in range(5):
    board.append(int(input()))

board.sort()

print(sum(board) // len(board))
print(board[2])
