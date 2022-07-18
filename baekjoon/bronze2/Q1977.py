import sys
import math

input = sys.stdin.readline

M = int(input())
N = int(input())

board = []

for i in range(M, N + 1):
    if math.sqrt(i).is_integer():
        board.append(i)

if len(board) == 0:
    print(-1)
else:
    print(sum(board))
    print(min(board))
