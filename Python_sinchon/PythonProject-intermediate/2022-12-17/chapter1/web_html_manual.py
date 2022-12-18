'''

파이선 활용하기

웹 크롤링

크롤링, 스크래핑
- API
- 웹페이지

HTML 이해
-> 웹 페이지를 만드는 언어
-> 태그, 속성

-> 태그 : 여닫는 꺽쇠괄호 안에 태그명을 사용
         대부분 여는 태그와 닫는 태그 싸응로 이루어져있음
<p>텍스트</p>
<h1>텍스트</h1>
<img src="보여줄 이미지 경로">, <video> : 닫는 태그가 없는 태그

        부모태그, 자식태그가 있음
        태그 안에 텍스트를 넣을 수 있는 태그가 있음
        img 태그와 같이 이미지를 보여주는 태그가 있음
        태그는 디자인을 하는 언어가 아님
        태그는 컨텐츠를 구분하는 언어

-> 속성 : 태그에 사용하는 것
         속성명과 값으로 이루어져있음

    id 속성 : 페이지 안에서 다른 태그와 구분하기 위해서
             태그에 id(식별자)를 부여해주는 속성
    class 속성 : 태그들을 묶을 때 부여해주는 속성
    id, class 차이 : id속성의 값은 중복되면 안됨
                    class 속성 값은 중복되도 됨
    태그 하나에 속성을 여려개 사용할 수 있음

브라우저의 개발자 도구 사용 방법
    -> 요소 선택 툴 : 웹 페이지 내 컨텐츠를 선택하는 도구
    -> 선택자 복사 : 그 태그(컨텐츠)를 경로를 복사하는 메뉴
    -> 검색 : Ctrl + F / 선택자를 제대로 입력했는지 확인할 수 있는 도구

라이브러리 설치하는 방법
-> pip 프로그램을 사용해서 설치
-> pip 프로그램은 명령을 사용해서 실행, 필요한 라이브러리를 설치

requests, BeautifulSoup 라이브러리
-> 개발이 오래 전에 완료된 프로젝트에서 사용
-> 간단하게 크롤링 테스트를 할 때 사용

셀레니움(Selenium) 라이브러리
-> 최근 개발 현장에서 사용되는 크롤링, 스크래핑 라이브러리

'''