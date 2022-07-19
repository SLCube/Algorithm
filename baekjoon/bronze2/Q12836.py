import sys

input = sys.stdin.readline

N, Q = map(int, input().split())

board = [0 for i in range(N)]
s = 0

for _ in range(Q):
    a, b, c = map(int, input().split())

    if a == 1:
        board[b - 1] += c
    elif a == 2:
        print(sum(board[b - 1:c]))
