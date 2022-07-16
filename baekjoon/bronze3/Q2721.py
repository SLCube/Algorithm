import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    Wn = 0
    n = int(input())
    for i in range(1, n + 1):
        Wn += i * (i + 1) * (i + 2) // 2

    print(Wn)

