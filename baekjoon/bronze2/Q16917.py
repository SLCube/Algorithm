import sys

input = sys.stdin.readline

A, B, C, X, Y = map(int, input().split())

sum = 0

if (A + B) < C * 2:
    print(A * X + B * Y)
else:
    m = min(X, Y)
    print(C * m * 2 + min(A, 2 * C) * max(0, X - Y) + min(B, C * 2) * max(0, Y - X))
