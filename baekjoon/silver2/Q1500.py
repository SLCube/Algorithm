import sys

input = sys.stdin.readline

S, K = map(int, input().split())

A = S // K
B = S % K
print(A ** (K - B) * (A + 1) ** B)
