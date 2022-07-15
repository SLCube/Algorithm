import sys

input = sys.stdin.readline

x, y = map(int, input().split())

x -= 1
y -= 1

d = abs(x // 4 - y // 4) + abs(x % 4 - y % 4)
print(d)