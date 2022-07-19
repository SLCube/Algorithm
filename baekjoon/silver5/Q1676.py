import sys

input = sys.stdin.readline

N = int(input())
cnt = 0
factorial = 1

for i in range(1, N + 1):
    factorial = factorial * i

for i in str(factorial)[::-1]:
    if i == '0':
        cnt += 1
    else:
        break

print(cnt)