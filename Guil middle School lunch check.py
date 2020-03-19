# author : 이현록
# 이 소스코드는 구일중학교의 급식정보를 구일중학교 공식 사이트에서 크롤링함으로서 동작합니다.
# 원리
# 0. input으로 날짜를 입력받는다.
# 1. http://guil.sen.ms.kr/65872/subMenu.do 사이트에 requests 모듈을 통해 날짜 정보를 POST 형식으로 보낸다.
# 2. Beautifulsoup을 통해 파싱을 한 뒤, a태그로 서버에 전송되는 mlsvId값을 찾아낸다.
# 3. 찾아낸 mlsvId값을 http://guil.sen.ms.kr/65872/subMenu.do 에 POST형식으로 보내서 급식정보를 얻는다.
# 4. 얻은 급식정보를 파싱 및 정규표현식으로 잘 가공한 뒤, print로 출력한다.
# v0.3 바뀐점
# class사용으로 객체화. 크게 mlsvId 값을 얻는 함수와 그 값을 토대로 최종 급식정보를 얻는 함수가 있음.
# 코드 최적화
# 급식 정보가 없는 요일에는 '해당 요일에는 급식이 없습니다.' 출력.

from bs4 import BeautifulSoup
import requests
import re
class Guilmeal:
    def get_mlsvid(self, date): #mlsvid값을 얻는 함수, 사용자로부터 date값을 입력받는다.
        filtering = re.compile('^(\d{4})-(\d{2})-(\d{2})') #date값 필터링
        mlsvid = 0

        filtered_date = filtering.match(date)
        if filtered_date == None:
            print('잘못된 값이 입력되었습니다.')
            return 0
        
        year, month, day = str(filtered_date.group(1)), str(filtered_date.group(2)), str(filtered_date.group(3)) # group 함수로 date로 입력받은 year, month, day를 각각 변수에 저장
        url = 'http://guil.sen.ms.kr/65872/subMenu.do'
        request_sent = requests.post(url, data={'viewType': ' calandar', 'viewType' : 'calendar', 'siteId': 'SEI_00001197', 'arrMlsvId':'0', 'srhMlsvYear':year, 'srhMlsvMonth':month})
        soup = BeautifulSoup(request_sent.text, 'html.parser')#mlsvid값을 얻기 위해 BeautifulSoup을 이용해 사이트를 파싱한다.
        soup2 = soup.find_all(title='클릭하면 내용을 보실 수 있습니다.')
        if day=='09':#re_text 정규표현식이 a태그 텍스트와 일치하도록 하기위해 day와 month의 값을 바꾼다
            day = '9'
        elif day=='08':
            day = '8'
        elif day=='07':
            day = '7'
        elif day=='06':
            day = '6'
        elif day=='05':
            day = '5'
        elif day=='04':
            day = '4'
        elif day=='03':
            day = '3'
        elif day=='02':
            day = '2'
        elif day=='01':
            day = '1'
        
        if month=='09':
            month = '9'
        elif month=='08':
            month = '8'
        elif month=='07':
            month = '7'
        elif month=='06':
            month = '6'
        elif month=='05':
            month = '5'
        elif month=='04':
            month = '4'
        elif month=='03':
            month = '3'
        elif month=='02':
            month = '2'
        elif month=='01':
            month = '1'
        re_text = re.compile(month+"월 "+day+"일 식단")
        re_fnDetail = re.compile("fnDetail\('(\d{7})'\);")

        for asdf in soup2:
            try:
                if re_text.search(asdf.text) != None:
                    mlsvid = (re_fnDetail.search(asdf['onclick'])).group(1)
            except:
                print('Error Occured!')
        if(mlsvid == 0):
            print('해당 요일에는 급식이 없습니다.')
            return 0
        self.mlsvid = mlsvid
        return 1
    
    def Getmeal(self):
        URL = 'http://guil.sen.ms.kr/dggb/module/mlsv/selectMlsvDetailPopup.do'
        rp = requests.post(URL, data={'mlsvId': self.mlsvid})
        soup = BeautifulSoup(rp.text, 'html.parser')
        soup_filtered = soup.find_all('tbody')
        soup_re = re.compile('[\t\r\f\v]')
        
        for meal in soup_filtered:
            print(soup_re.sub('', str(meal.text)))
        

print("""
author : lee hyun rok
제작자 : 이현록
구일중 급식체크 프로그램입니다.
8글자로 날짜를 입력해 주세요
예시 : 2019-06-18(2019년 6월 18일)
v0.3
""")


while True:
    date = input('날짜 입력 : ')
    guilmeal = Guilmeal()
    if guilmeal.get_mlsvid(date) == 0:
        continue
    else:
        print(guilmeal.mlsvid)
        guilmeal.Getmeal()
        break

input("종료하려면 아무 키나 누르세요...")
