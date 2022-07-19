import sys

input = sys.stdin.readline

aCards = list(map(int, input().split()))
bCards = list(map(int, input().split()))

aWins = 0
bWins = 0

for i in range(10):
    if aCards[i] > bCards[i]:
        aWins += 1
    elif aCards[i] < bCards[i]:
        bWins += 1

if aWins > bWins:
    print('A')
elif aWins < bWins:
    print('B')
else:
    print('D')