#file_read

#파일 오픈(읽기모드)
file = open('./day03/second_file.txt','r', encoding= 'utf-8')

#파일 읽고
content = file.read() # 파일을 하나의 문자열로 읽어서 변수 content 에 담는다
# 텍스트파일 용량이 너무 크면 읽어오는 도중에 비정상 종료됨(error)
print(content)


#파일 닫기
file.close()

print('파일 통으로 읽음')


#파일 오픈
file2 = open('./day03/my_first_file.txt', 'r', encoding = 'utf-8')

#일반적인 파일에서 문자열 읽기
while True :
    line = file2.readline() # 한줄씩 읽어서 line 변수에 담는다
    if not line : # 읽은줄에 글자가 한 글자도 없다면
        break
    print(line, end ='') # print 함수의 end 기본파라미터값 \n을 제거

#파일 닫기
file2.close()

print('파일 한줄읽기 완')

