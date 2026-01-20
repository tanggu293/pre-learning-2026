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
     ''`
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
        - 문장을 작성할 시 **강조** ~~취소~~ 선, __강조__. <u>밑줄</u>,<i>이탤릭<i> 을 사용할 수 있습니다. 
