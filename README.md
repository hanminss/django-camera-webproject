# CameraProject
카메라 프로젝트

2020 0817 석근
렌즈/바디 별  별점 평균을 내림차순 정렬하여 가져와서 출력하는 데에는 성공했지만
1위 2위 3위 이렇게 인덱스 증가하면서 어떻게 출력해줄지 모르겠습니다,, 검색해봤는데 {{ forloop.counter }} 쓰면 된다는데 안돼요

2020 0818 석근
한민형 상준형과 고민끝에 모델을 갈기로 결정, lenstype bodytype 모델은 더이상 사용하지않고 Type으로 바디/렌즈로만
나눠주기로 함. views들을  고쳐야함. 참고로 외래키이므로 Product에서 타입을 결정할 땐 pdtype_id = 1  or  2  로 사용하기바람. (1 :바디 ,2 : 렌즈)

2020 08 13 ----------------
Merge branch test(정수빈)
1. 제품 디테일 프론트 제작
2. 마이페이지 프론트 제작

2020 08 14 ----------------
Merge branch 유진아 마이페이지
1. 마이페이지 수정

한민 master 수정
1. 마이페이지 view 작성(login.html 없어서 오류)
2. 로그인 , 로그아웃, 회원가입 완성
수빈
1. 로그인페이지, 마이페이지 연결
2. 제품 디테일 백, 프론트 수정
3. 내정보 백,프론트 완성
4. 마이페이지 html 수정

진아
1. 마이리뷰 뷰 작성
2. 로그인 회원가입 프론트

석희, 석근
2020 0818 석근
자 바꾼 model로 main.views와 main.templates들 수정완료 (item_detail,album_detail 제외) 완료!!!!!!!!!!!!!!!!!랭크도 모두 구현완료


2020 0820 석근
1. Product 모델
lenstype bodytype 모델은및외래키는 사용하지않고 Type으로 바디/렌즈로 나눠주기로 함. 
바디 or 렌즈 만을 선택하는 pdtype Foreignkey (Type) 필드로 통일하고세부 이름은 pdname에 씁니다
 외래키이므로 Product에서 타입을 결정할 땐 pdtype_id = 1  or  2  로 사용하기바람. (1 :바디 ,2 : 렌즈)
 (+lenstype,bodytype , stars (Integer)필드 삭제@)
2. item_detail 수정 및 리뷰 리스트 뜨도록 추가, 또한 create_review까지 가능하도록 함. 
3. album_detail 까지 완료