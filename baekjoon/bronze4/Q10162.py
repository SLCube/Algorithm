import sys

T = int(input())

A = T // 300
T -= 300 * A

B = T // 60
T -= 60 * B

C = T // 10
T -= 10 * C

if T != 0:
    print(-1)
else:
    print(A, B, C)