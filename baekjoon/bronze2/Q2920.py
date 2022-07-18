import sys
import copy

board = list(map(int, input().split()))

ascending = copy.deepcopy(board)
ascending.sort()
descending = copy.deepcopy(board)
descending.sort(reverse=True)

if board == ascending:
    print('ascending')
elif board == descending:
    print('descending')
else:
    print('mixed')