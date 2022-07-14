import sys

x, y, w, h = map(int, input().split())

d1 = x if w - x > x else w - x
d2 = y if h - y > y else h - y

if d1 < d2:
    print(d1)
else:
    print(d2)
