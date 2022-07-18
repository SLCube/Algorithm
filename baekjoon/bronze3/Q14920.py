import sys

input = sys.stdin.readline

N = int(input())
cnt = 1

while True:
    if N == 1:
        break
    elif N % 2 == 0:
        N //= 2
    elif N % 2 == 1:
        N = 3 * N + 1
    cnt += 1

print(cnt)
