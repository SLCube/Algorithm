import sys

input = sys.stdin.readline

N = int(input())

cnt = 0

seat = list(int(i) for i in range(1, 101))

board = list(int(x) for x in input().split())

for i in board:
    if seat.count(i) != 0:
        seat.remove(i)
    else:
        cnt += 1

print(cnt)