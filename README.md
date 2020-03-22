author : 이현록

이 소스코드는 구일중학교의 급식정보를 구일중학교 공식 사이트에서 크롤링함으로서 동작합니다.

사용 프로그램 : v0.1~v0.2 : Python IDLE, v0.3 : Visual Studio Code

############원리 (v0.2~)

0. input으로 날짜를 입력받는다.

1. http://guil.sen.ms.kr/65872/subMenu.do 사이트에 requests 모듈을 통해 날짜 정보를 POST 형식으로 보낸다.

2. Beautifulsoup을 통해 파싱을 한 뒤, a태그로 서버에 전송되는 mlsvId값을 찾아낸다.

3. 찾아낸 mlsvId값을 http://guil.sen.ms.kr/65872/subMenu.do 에 POST형식으로 보내서 급식정보를 얻는다.

4. 얻은 급식정보를 파싱 및 정규표현식으로 잘 가공한 뒤, print로 출력한다.

정보)
http://guil.sen.ms.kr/65872/subMenu.do 사이트에 POST방식으로 viewType, siteId, arrMlsvId, srhMlsvYear, srhMlsvMonth값을 보내야 해당 년월일의 a태그에 내장된 mlsvId값을 알 수 있는데, siteId값과 viewType, arrMlsvId값은 고정값이므로 그냥 냅두고 srhMlsYear와 srhMlsvMonth 값에 각각 날짜 정보를 넣으면 해당 년, 달 의 mlsvId를 내장한 a태그들을 얻을 수 있다.

정보2)
http://guil.sen.ms.kr/dggb/module/mlsv/selectMlsvDetailPopup.do 사이트에 날마다 다른 mlsvId 값을 requests를 이용해 POST방식으로 보내면 급식 정보를 뱉어낸다

#############

v0.1

최초 출시 - mlsvId값을 사용자가 직접 입력해야 작동함(완전하지 않음)

버그1 - 문자열 입력 시 프로그램이 자동으로 종료됨

#############

v0.2

사용자가 mlsvId값을 직접 입력하지 않고 날짜만 입력해도 급식정보가 나타나도록 수정됨

버그1 - 급식 정보가 없는 날(토요일, 일요일, 공휴일)에는 에러가 출력됨

버그2 - 문자열, 공백 입력 시 아무 출력 없이 프로그램 종료됨



##############

v0.3

코드 관련

 -> 코드 안정화 및 최적화 진행됨

 -> class사용으로 객체화 시킴. 크게 mlsvId 값을 얻는 함수와 mlsvId값을 토대로 최종 급식정보를 얻는 함수가 있음.

기능 관련

 -> 급식 정보가 없는 요일에는 '해당 요일에는 급식이 없습니다.' 출력

 -> 잘못된 값 입력시 '잘못된 값이 입력되었습니다.' 출력 및 다시 날짜 물어봄

버그 수정

v0.2의 버그1, 버그2 해결됨.

#############

v0.4

기능 관련

-> 정규표현식으로 급식 정보, kcal 정보를 변수 안에 저장한 뒤, 출력함
