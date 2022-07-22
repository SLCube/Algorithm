import sys
import math

input = sys.stdin.readline

A, B = map(int, input().split())

result = 1

if math.gcd(A, B) == 1:
    result = A * B
else:
    result = (A // math.gcd(A, B)) * (B // math.gcd(A, B)) * math.gcd(A, B)

print(result)