# Algorithm

----

python을 이용한 알고리즘 학습

- 백준 문제 풀이

---

- Java vs Python 문법 차이
1. 반복문
- Java
```java
for(int i = 0 ; i < 10; i++){
    System.out.println(i);
}
```
-python
```python
for i in range(10):
    print(i)
```

2. 조건문
- Java
```java
int num = 1

if(num == 1) {
    System.out.println("num은 1입니다");
} else {
    System.out.println("num은 1이 아닙니다");
}
```

- python
```python
num = 1
if num == 1:
    print("num은 1입니다.")
else:
    print("num은 1이 아닙니다.")
```

3. python의 for ~ else 구문
```python
for i in range(5):
    if i == 3:
        break

else:
    print("반복문이 정상적으로 완료되었습니다.")
```

4. 삼항 연산자
```java
Type 변수명 = 조건 ? 참 : 거짓;

int a = 10;
int b = 20;

int c = b >= a ? 100 : 200;
System.out.println(c) // c = 100 
```

```python
a = 10
b = 20
c = 100 if b >= a else 200
print(c) # c = 100
```