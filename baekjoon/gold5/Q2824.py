import sys

input = sys.stdin.readline

N = int(input())
board = [int(x) for x in input().split()]

A = 1
for i in board:
    A *= i
board.clear()

M = int(input())
board = [int(x) for x in input().split()]

B = 1
for i in board:
    B *= i
board.clear()
C = max(A, B)
D = min(A, B)

while C % D != 0:
    C, D = D, C % D

if len(str(D)) > 9:
    print(str(D)[len(str(D)) - 9: len(str(D))])
else:
    print(D)