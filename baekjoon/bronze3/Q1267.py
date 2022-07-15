import sys

input = sys.stdin.readline

n = int(input())

d = [int(x) for x in input().split()]

Y = 0
M = 0

for i in range(n):
    Y += (d[i] // 30 + 1) * 10
    M += (d[i] // 60 + 1) * 15

if M < Y:
    print(f"M {M}")
elif Y < M:
    print(f"Y {Y}")
else:
    print(f"Y M {Y}")
