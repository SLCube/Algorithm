import sys

cnt = 0

while True:
    s = input()
    if s == '#':
        break
    for ch in s:
        if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
            cnt += 1
    print(cnt)
    cnt = 0
