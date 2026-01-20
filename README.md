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

  9. cmd 또는 pwershell 오픈, `pyhon --version` 확인
  
  10.VS Code , extension(확장)에서 python 검색 후 설치
     
  - 프로그램 개발 개념
