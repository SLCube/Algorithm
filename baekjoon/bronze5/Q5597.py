import sys

studentNumList = list(range(1, 31))

for _ in range(28):
    studentNumList.remove(int(input()))

studentNumList.sort()

for i in studentNumList:
    print(i)