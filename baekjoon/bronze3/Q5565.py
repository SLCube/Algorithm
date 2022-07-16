import sys

input = sys.stdin.readline

total = int(input())
board = []
for _ in range(9):
    board.append(int(input()))

print(total - sum(board))