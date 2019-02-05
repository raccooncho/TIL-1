import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time, datetime

driver = webdriver.Chrome('C:/Users/이상택/chromedriver.exe')
url = 'https://edu.ssafy.com/comm/login/SecurityLoginForm.do'
driver.get(url)

user_id = 'srs99125@naver.com'
user_pwd = '##qQ036578'

driver.find_element_by_name('userId').send_keys(user_id)
driver.find_element_by_name('userPwd').send_keys(user_pwd)
driver.find_element_by_xpath('//*[@id="wrap"]/div/div/div[4]/form/div/div[2]/div[3]/a').click()

driver.get('https://edu.ssafy.com/edu/mycampus/attendance/attendanceList.do')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

today = time.strftime("%Y-%m-%d")
# for test
today= '2019-01-30'

check_in_out = soup.select(f'a.fc-day-grid-event.fc-h-event.fc-event.fc-start.fc-end.cate.at01.event-on-{today}')
early_check_out = soup.select(f'a.fc-day-grid-event.fc-h-event.fc-event.fc-start.fc-end.cate.at02.event-on-{today}')
check = len(check_in_out)
early = len(early_check_out)
if check == 0:
    print('아직 출석하지 않으셨습니다!')
if check == 1:
    if early == 1:
        print(f'{early_check_out[0].text}')
    else:
        print('아직 퇴실하지 않으셨습니다!')
if check == 2:    
    if int(check_in_out[1].text[0:2]) < 18:
        print('18시 이전에 퇴실 버튼을 누르셨습니다!')
    else:
        print(f'{check_in_out[0].text}')
        print(f'{check_in_out[1].text}')