#functions.py
# def 함수명([매개변수]):
#   함수내코드 작성
# == parameter == (arguement)

# 내장함수사용
print()
print('Hello Python')
print(str(10))

# 함수 정의 (매개변수없는 것)
def sayHello1():
    #pass # 코드오류 방지기능 팁
    print('hi')
    ####return None 이 숨어있는 형태
# 매개변수 사용 
def sayHello2(name):
    #"" ''
    print("hi i'm " + name)

#매개변수사용 + 반환(리턴)
def add(x,y):  
    result = x + y
    return result 

#매개변수 없이 반환하는 함수
def process():
    result = 'Done'
    return result

#def get_user_info(id):  
    # DB에서 개인정보를 가져옴
   # info = None
    #return info

# 커스텀함수 사용(호출)
sayHello1()

#함수호출(매개변수사용)
sayHello2('민수')
sayHello2('민슈')

sum = add(10,5)
# sum = 15
print(sum)

print(process())
# print('Done')와 동일

