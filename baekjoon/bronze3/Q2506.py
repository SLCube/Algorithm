import sys

input = sys.stdin.readline

N = int(input())

answer = [int(x) for x in input().split()]

score = 1
s = 0
for i in range(N):
    if answer[i] == 1:
        s += score
        score += 1
    elif answer[i] == 0:
        score = 1

print(s)
