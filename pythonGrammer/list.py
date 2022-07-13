# import random as r
#
# b = list()
# # print(b)
#
# a = [1, 2, 3, 4, 5]
# # print(a)
# # print(a[0])
#
# b = list(range(1, 11))
# # print(b)
#
# c = a + b
# # print(c)
#
# # print(a)
# a.append(6)  # 리스트 뒤에 요소를 추가하는 함수
# # print(a)
#
# a.insert(3, 7)
# # print(a)
#
# a.pop()
# # print(a)
# a.pop(3)
# # print(a)
#
# a.remove(4)
# # print(a)
#
# # print(a.index(5))
#
# a = list(range(1, 11))
# print(a)
# print(sum(a))
# print(max(a))
# print(min(a))
# print(min(7, 5))
# print(min(7, 3, 5))
# print(a)
# r.shuffle(a)
# print(a)
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# a.clear()
# print(a)

a = [23, 12, 36, 53, 19]
print(a[:3])
print(a[1:4])
print(len(a))

for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a:
    print(x, end=' ')
print()

for x in a:
    if x % 2 == 1:
        print(x, end=' ')
print()

for x in enumerate(a):
    print(x, end=' ')
print()

b = (1, 2, 3, 4, 5)  # 대괄호는 list 소괄호는 tuple이다. tuple은 값 변경이 불가하다. list는 가능하다.
print(b[0])

for x in enumerate(a):
    print(x[0], x[1])
print()

for index, value in enumerate(a):
    print(index, value)
print()

if all(50 > x for x in a):
    print("YES")
else:
    print("NO")

if any(50 > x for x in a):
    print("YES")
else:
    print("NO")
print()

# a = [0] * 3
# print(a)

a = [[0] * 3 for _ in range(3)]
print(a)

for x in a:
    print(x)
print()

for x in a:
    for y in x:
        print(y, end=' ')
    print()
