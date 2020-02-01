#author : 이현록
#이 소스코드는 구일중학교의 급식정보를 구일중학교 공식 사이트에서 크롤링함으로서 동작합니다.



from bs4 import BeautifulSoup
import requests
import re

def GetMeals(date):
    
    filtering = re.compile('^(\d{4})-(\d{2})-(\d{2})') #date 필터링 위한 정규표현식 생성
    if date == '': #문자 형식 이상할시 끝냄
        return 1
    elif filtering.search(date) == None:
        return 2
    filtered_date = filtering.search(date) #매칭한 날짜 넣음
    
    year = str(filtered_date.group(1))#정규표현식 그룹을 통한 숫자 지정
    month = str(filtered_date.group(2))
    day = str(filtered_date.group(3))

    daylink = 'http://guil.sen.ms.kr/65872/subMenu.do'
    mlsvid_sub_soup = requests.post(daylink, data={'viewType' : 'calendar', 'siteId': 'SEI_00001197', 'arrMlsvId':'0', 'srhMlsvYear':year, 'srhMlsvMonth':month})
    mlsvid_main_soup = BeautifulSoup(mlsvid_sub_soup.text, 'html.parser')#mlsvid값을 얻기 위해 BeautifulSoup을 이용해 사이트를 파싱한다.
    nomeal1 = mlsvid_main_soup.find_all(title='클릭하면 내용을 보실 수 있습니다.')#a태그만 얻기위해 걸러낸다.
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
    for nomeal in nomeal1:
        try:
            if re_text.search(nomeal.text) != None:
                mlsvid = (re_fnDetail.search(nomeal['onclick'])).group(1)
        except ValueError :
            print('Error Occured!')




    
    baseURL = "http://guil.sen.ms.kr/dggb/module/mlsv/selectMlsvDetailPopup.do"
    rd = requests.post(baseURL, data={'mlsvId': mlsvid})    
    soup = BeautifulSoup(rd.text, 'html.parser')
    meals = soup.find_all('tbody')
    p = re.compile('[\t\r\f\v]')

    LIL = ''
    for meal in meals:
        print(p.sub('', str(meal.text)))
        
    return 0

#def switch(x):
#    print({0:'Successfully data sent.', 1:'Error 1 : no data sent', 3:'Something wrong!'}.get (x, "default"))




    
print("""
author : lee hyun rok
제작자 : 이현록
구일중 급식체크 프로그램입니다.
8글자로 날짜를 입력해 주세요
예시 : 2019-06-18(2019년 6월 18일)
""")

date = input('날짜 입력 : ')
GetMeals(date)
input("Enter키를 눌러 종료합니다...")
