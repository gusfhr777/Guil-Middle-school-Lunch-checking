#author : lee hyun rok

from bs4 import BeautifulSoup
import requests
import re

def getMeals(date=''):
    if (date==''):
        print('Error1 : Data Not Found\n데이터가 입력되지 않았습니다. 실행을 종료합니다.')
        return 0
    ㄴ
    baseURL = "http://guil.sen.ms.kr/dggb/module/mlsv/selectMlsvDetailPopup.do"
    rd = requests.post(baseURL, data={'mlsvId': date})    
    soup = BeautifulSoup(rd.text, 'html.parser')
    meals = soup.find_all('tbody')
    p = re.compile('[\t\r\f\v]')

    LIL = ''
    for meal in meals:
        print(p.sub('', str(meal.text)))


print("""
author : lee hyun rok
구일중 급식체크 프로그램입니다.
8글자로 날짜를 입력해 주세요
예시 : 20190618(2019년 6월 18일)
""")

user_date = input('날짜 입력 : ')

getMeals(user_date)
