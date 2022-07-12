# Algorithm

----

python을 이용한 알고리즘 학습

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