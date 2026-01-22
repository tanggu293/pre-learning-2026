# moduels.py - 모듈 내장함수 확인
# import 모듈명

import math # 수학관련 함수와 데이터 담고있는 모듈

pi = 3.141592

radius = 10
result = radius * radius * pi
print('간단 원의넓이는'+ str(result))

result = radius * radius * math.pi #모듈안에 있는 pi
print(math.pi)
print('복잡 원의 넓이는' + str(result))

# 수학 모듈

print(math.sqrt(16))
print(math.floor(4.3)) # 바닥. 숫자 내림
print(math.ceil(4.2))


import datetime # 날짜, 시간 모듈

print(datetime.datetime.now())

## 내장함수
# 배열, 문자열 길이리턴 함수
print(len('Hello')) # 문자열길이 : 5 
print(len([1,2,3,4,5,6])) # 6나옴


# 데이터형 확인 함수
print(type(1))
print(type(pi))
print(type([1,2,3,4]))
print(type('Hello'))


print(int('80')) #정수형으로 된 문자열만 변환가능
print(float('4')) # 정수형, 실수형 모두 변환 가능
print(str(3.141592))
print(int(80.4))




