import sys

input = sys.stdin.readline

h, m, s = map(int, input().split())

q = int(input())

for _ in range(q):
    li = list(map(int, input().split()))

    if len(li) == 1 and li[0] == 3:
        print(h, m, s)
        continue
    else:
        t = 3600 * h + 60 * m + s

        if li[0] == 1:
            t += li[1]
        else:
            t -= li[1]

        if t < 0:
            t += 86400

        t %= 86400

        h, m, s = t // 3600, (t % 3600) // 60, t % 60