import sys
import math

input = sys.stdin.readline

G, L = map(int, input().split())

C = L // G
result = 0
for i in range(math.floor(math.sqrt(C)), 0, -1):
    if C % i == 0 and math.gcd(i, C // i) == 1:
        result = i
        break

print(G * result, (C // result) * G)