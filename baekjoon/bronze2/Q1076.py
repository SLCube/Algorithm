import sys

input = sys.stdin.readline

resistance = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7, 'grey': 8,
              'white': 9}
C1 = input()
C2 = input()
C3 = input()
R1 = resistance[C1[:len(C1) - 1]]
R2 = resistance[C2[:len(C2) - 1]]
R3 = resistance[C3[:len(C3) - 1]]
print((R1 * 10 + R2) * (10 ** R3))
