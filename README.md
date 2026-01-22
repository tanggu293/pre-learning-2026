# pre-learning-2026
IoT개발자 과정 사전학습 리포지토리

## 1일차
과정소개

학습 리포지토리 생성

- 마크다운 문법
  1. 제목
    ```markdown
    # 제목1
    ## 제목2
    ### 제목3
    #### 제목4
    ##### 제목5
    ###### 제목6 ( 잘사용안함)
    <!-- 주석(HTML주석 동일) -->
    ```

  2. 목록
    ```markdown
    - 목록
    * 목록
    1. 숫자목록
    2. 숫자목록
    ```

    3. 링크, 이미지
       
  ```markdown
  [네이버](https://naver.com)

  ![이미지](이미지URL)

   ## 사이즈 조절 이미지
  src : 이미지URL
  width : 이미지넓이 픽셀단위 지정
  <img src="이미지URL" width="500">

   ```

    - [네이버](https://naver.com)
   
    - ![강남](https://naverpa-phinf.pstatic.net/MjAyNjAxMDZfNjUg/MDAxNzY3Njc1OTQ1NzQ1.LUDf36_DqwqfFNOVFr3bA2BMNefn1oGd9iv_Lry60g8g.1ZuVNZBSKtH7Wx01NAAL6BdXF9HJ7jW0mZyvvw8W15og.JPEG/0_342x228_176767594573317555301678645804685.jpg)
    - <img src="https://naverpa-phinf.pstatic.net/MjAyNjAxMDZfNjUg/MDAxNzY3Njc1OTQ1NzQ1.LUDf36_DqwqfFNOVFr3bA2BMNefn1oGd9iv_Lry60g8g.1ZuVNZBSKtH7Wx01NAAL6BdXF9HJ7jW0mZyvvw8W15og.JPEG/0_342x228_176767594573317555301678645804685.jpg" width="300">
    -이미지와 링크의 차이는 !로시작하는지 밖에 없음 

 - <img width="703" height ="463" alt ="image" src="https://lh3.googleusercontent.com/gps-cs-s/AG0ilSxw_hj1QVGq0qsmKF1LdpJPicLOrn_lb3yKMHzGCRp_q4tMzN_c6Yhvrj5Dv3E5VCcnyUhh7c28iBKg3o0AP6Ixj-at4OxGauld2y7twY8_lf-BxG-PnL3LUHXkCzqwLhyPh4g8=s680-w680-h510-rw">

   4. 가로줄
     ```markdown
     ---
     ```
---
   5. 코드블럭
     - 소스코드를 작성할 때 코드하이라이팅, 영역표시 때 사용
     - 백틱(`)을 세번 후 표시언어를 입력 또는 한번(인라인 코드블럭)
     ```python
     print('hello, python!')
     ```
     
   - 일반적인 문장에서 한 단어를 강조하고 싶을때 `인라인 코드블럭`을 사용
   
     6. 강조 및 밑줄
        ```markdown
        *,~,__, html u 태그사용, i 이탤릭 사용
        ```
        - 문장을 작성할 시 **강조** ~~취소~~ 선, __강조__. <u>밑줄</u>,<i>이탤릭</i>을 사용할 수 있습니다. 




 - 깃허브 로컬리포지토리 생성
  1. git for Windows 설치
     - https://git-scm.com/install/windows 에서 `install for windows` 버튼 클릭
     - Git for windows x64 설치
     - Git 설치 옵션은 기본 그대로 사용 가능(변경하지 말 것)
     - cmd 또는 powershell 에서 `git --version`, `git -v` 확인
  3. Github Desktop 설치
    - https://github.com/apps/desktop?locale=ko-KR 에서 다운로드 클릭, 설치
    - 계정 브라우저 연동 
  4. 리포지토리 클론
     - Github Desktop 메뉴 Clone Repository 클릭
     - Github.com 탭에서 저장소 검색, 선택
     - Local Path 지정 후 `클론` 버튼 클릭
    
 - Visual Studio Code 설치
   1. https://code.visualstudio.com/Download for windows 버튼 클릭
   2. 설치 C:\DEV\IDE\Microsoft VS Code에 설치
   3. Extensions > Korean Pack for visual Studio Code 설치 후 재시작

- 추가 설치 프로그램
  1. Notepad ++ 에디터 https://notepad-plus-plus.org/downloads/v8.9/
  2. 픽픽 - https://picpick.net
  
- **파이썬** 개발환경 설정
  1. https://www.python.org/ 에서download의 `python 3.1x.x 버튼클릭`
  2. Add python.exe. to PATH 체크 활성화 후
  3. Installer > Customize installation 클릭
  4. Documentation 체크 해제, For all users 체크 활성화 다음
  5. Advanced Options 에서 Install Python 3.1x for all users 체크
  6. 경로 변경후 설치
    <img width="660" height="422" alt="image" src="https://github.com/user-attachments/assets/72048b6c-8874-4ce8-8137-f8bf8c18adcf" />

  8. Setup was successful 에서 Disable path length limit 클릭(필수!)
     <img width="752" height="455" alt="image" src="https://github.com/user-attachments/assets/31a3b4c8-c3e7-4250-a64b-afe6fca3a9ae" />

  9. cmd 또는 powershell 오픈, `python --version` 확인
  
  10.VS Code , extension(확장)에서 python 검색 후 설치

  11. VS Code를 재오픈 폴더 생성
  
 ##2일차

 - VS Code 설정
  1.  미니맵 설정 : 설정 > 미니맵 검색,
    - Editor > Minimap : Enabled 체크 해제
  2.  폰트 지정
    - 나눔고딕코딩, D2Coding 등 한글지원 코딩글자체 사용
    - https://github.com/naver/nanumfont
    - 설정 > Editor : Font Family 맨앞에, NanumGothicCoding, 입력
  3.  Mouse Wheel Zoom : 체크 활성화
         
  - 프로그램 개발 개념
    - 프로그램: 데이터를 처리하는 명령을 수행하는 것
    
    - 단순구조 : 데이터를 직접 처리하는 프로그램

      ![alt text](image.png)

  - DB사용구조 : 데이터를 DB 에서 저장, 프로그램에서 데이터 처리( 전송 및 표현 )
    ![alt text](image-1.png)
    - DB가 같은 컴퓨터에 존재할 수도 있고, 다른 컴퓨터(서버)에 존재할 수 있음

  - IoT확장구조 : 데이터는 IoT에서 수집, 통신프로그램도 분리, 서버도 분리
    ![alt text](image-2.png)
    - 클라우드나 가상머신을 사용할 수도 있음

  - 학습할 언어, 기술
    - C, C++
    - DataBSE(MySQL) : IoT장비와 같이 사용하기 위함
    - Python
    - C# : WinApp, WebApp(HTML, JS, ...), IoT 모니터링, DB처리...
    - Linux : ROS, 라즈베리파이 OS 
    - 네트워크 통신, Iot, 데이터분석(ML,DL), 알고리즘, 코딩테스트




- 파이썬
  - 기본문법  
    - 변수와 자료형 
    - 제어문(if,while,for ..조건문, 반복문)
    - 함수(또는 메서드)
    - 파일 입출력
    - 객체지향
    - 예외처리

- 변수와 자료형
    - [변수](./day02/variable.py) 확인
    - [자료형](./datatype.py)

- 제어문
  - [if문](./day02/if_statement.py) 확인
  - [while문](./day02/while_statement.py) 확인
  - [for문](./day02/for_statement.py) 확인

##3일차
- 파이썬 
  - 함수 및 모듈
    - [함수](./day03/functions.py) 확인
    - [모듈](./day03/modules.py) 확인
  - 개념
    - 컴퓨터는 모든 것이 값
    - ENTER('\n'), SPACE(32), ""(EMPTY) 도 값, None(미정) == Null
