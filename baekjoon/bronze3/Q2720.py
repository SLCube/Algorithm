import sys

input = sys.stdin.readline

quater = 0  # 25C
dime = 0  # 10C
nickel = 0  # 5C
penny = 0  # 1C

T = int(input())

for _ in range(T):
    C = int(input())

    quater = C // 25
    C -= quater * 25

    dime = C // 10
    C -= dime * 10

    nickel = C // 5
    C -= nickel * 5

    penny = C

    print(quater, dime, nickel, penny)

    quater, dime, nickel, penny = 0, 0, 0, 0
