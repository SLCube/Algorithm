import sys

input = sys.stdin.readline

basic = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W',
         'X', 'Y', 'Z']

caesar = ['D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
          'X', 'Y', 'Z', 'A', 'B', 'C']

s = input()

for i in s[:len(s) - 1]:
    print(basic[caesar.index(i)], end='')
