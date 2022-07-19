import sys

input = sys.stdin.readline

X = int(input())
print(bin(X)[2:].count('1'))