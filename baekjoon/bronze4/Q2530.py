import sys

hour, minute, second = map(int, input().split())
period = int(input())

second += period
minute += second // 60
hour += minute // 60

if second >= 60:
    second %= 60

if minute >= 60:
    minute %= 60

if hour >= 24:
    hour %= 24

print(hour, minute, second)
