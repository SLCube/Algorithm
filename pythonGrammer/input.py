'''
a = input("숫자를 입력해주세요 : ")
print(a)
'''
'''
일반 input()을 이용하면 string type이 들어온다.
'''
'''
a, b = input("숫자를 입력해주세요 : ").split()
print(type(a))
print(type(b))
c = a + b
print(type(c))
print(c)
print(a + b)
'''

# a, b = input("숫자를 입력해주세요 : ").split()
#
# a = int(a)
# b = int(b)
#
# print(a + b)

# a, b = map(int, input('숫자를 입력해주세요 : ').split())
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)  # // 연산자 : 몫을 나타내줌
# print(a % b)
# print(a ** b)

# a = 4.3
# b = 5
# c = a + b
#
# print(type(a))
# print(type(b))
# print(type(c))

# 반복문

# a = range(1, 11)
#
# print(list(a))

# for i in range(10):
#     print("hello", i)
#
# for i in range(10, 0, -1):
#     print(i)

# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# i = 10
# while i >= 1:
#     print(i)
#     i -= 1

# i = 1
# while True:
#     print(i)
#     i += 1
#     if i == 12:
#         break

# for i in range(1, 11):
#     if i % 2 == 0:
#         continue
#     print(i)

# python for else -> 정상적으로 for문이 끝나면 else구문을 실행함.

# for i in range(1, 11):
#     print(i)
#     if i == 5:
#         break
# else:
#     print(11)

n = int(input('숫자를 입력해주세요 : '))

for i in range(1, n + 1):
    if i % 2 == 1:
        print(i)

print('====================')

sum = 0

for i in range(1, n + 1):
    sum += i

print(sum)

print('====================')

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=' ')
