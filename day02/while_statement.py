# while_statement.py - 반복문 중 while 문
# while (조건이 참인 동안):
# 반복문
import time

# 카운트다운
# count = 10

# while count > 0:
#     print(count)
#     count = count - 1
#     time.sleep(1)   #1초 대기

# print('발사!')

# count = 1

# while count > 0:
#     print(count)
#     count = count + 1
#     time.sleep(0.2)

# print('프로그램종료')    

# 입력에 따른 프로그램 종류
# count = 1
# while True :
#     user_input = input('종료하려면 exit를 입력하세요')
#     if user_input == 'exit':
#         print('반복문 탈출')
#         break #반복문 탈출
#     else:
#         count = count + 1
#         print(count)
#         print('사용자 입력 : ' + user_input)
# print('프로그램 종료')

#countinue : 어떤 조건만 뛰어넘고 반복 계속
number = 0

while number < 10: # number 가 10보다 작을 동안
    number += 1 # number = number + 1
  
    if number ==3 or number ==6 or number == 9:
        print('짝ㄱㄱ')
        continue
    print(number)

print('프로그램 종료')
