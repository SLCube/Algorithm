import sys
import math

input = sys.stdin.readline

T = int(input())

board = list(map(int, input().split()))
total = 0

for i in board:
    for j in range(1, i + 1):
        if i % j == 0:
            total += j

    total -= i

    if total == i:
        print("Perfect")
    elif total > i:
        print("Abundant")
    else:
        print("Deficient")

    total = 0