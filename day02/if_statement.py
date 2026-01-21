#if_statement.py - 제어문 if 문
# 제어문 중 최초로 만들어진 것
# if  조건: 참인 조건 
#       처리할 문장
# else:
#       처리할 문장

age = 16

print('담배주세요')

if age > 19: # 항상 참인 조건
    print("담배를 산다")
else: # 거짓인 조건
    print("민증이요")



blood = 'A' #B, AB, O

if blood == 'A':
    print('ㅇㄹㅇㄹ')
elif blood == 'B':  
    print("ㅋㅋㅋ")
elif blood == 'AB':
    print('gfdf')
elif blood == 'O' :
    Print('good')
else:
    print('ㅎㅎㅎㅎ')

print() #줄 띄어줌

is_adult = True
gender = 'Female'


# 이중 if문으로 분기
if is_adult == True:
   print('대인입니다 200000원')
   if gender == 'Male':
      print('남탕으로가삼')
   else:
       print('여탕 ㄱㄱ')
    

# 논리연산자 and로 분기
is_adult = False
gender = 'Male'
if (is_adult == True and gender == 'Male'):
    print('대인, 남자입니다 200000')
elif is_adult == True and gender == 'Female':
    print('대인 여자 200000')
elif is_adult == False and gender == 'Male':
    print('소인 남자입니다 5100')
elif is_adult == False and gender == 'Female':
    print('소인 남자입니다 5100')

#and, or , not
print(not is_adult)
