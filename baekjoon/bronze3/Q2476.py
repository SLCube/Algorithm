import sys

input = sys.stdin.readline

N = int(input())

maxMoney = []

for _ in range(N):
    x, y, z = map(int, input().split())

    if x == y == z:
        maxMoney.append(10000 + x * 1000)
    elif x == y:
        maxMoney.append(1000 + x * 100)
    elif y == z:
        maxMoney.append(1000 + y * 100)
    elif z == x:
        maxMoney.append(1000 + z * 100)
    else:
        maxMoney.append(100 * max(x, y, z))

print(max(maxMoney))