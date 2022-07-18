import sys

input = sys.stdin.readline

board = list(map(int, input().split()))

board.sort()

print(board[1])
