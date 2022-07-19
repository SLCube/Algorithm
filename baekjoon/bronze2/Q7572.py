import sys

input = sys.stdin.readline

gan = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ez = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']

N = int(input())

N = N - 4

print(f'{ez[N%12]}{gan[N%10]}')