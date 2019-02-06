import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time, datetime
import schedule  #pip install schedule 필요
# schedule 모듈 document : https://schedule.readthedocs.io/en/stable/

def lunch_menu(user_id, user_pwd, driver_location):
    driver = webdriver.Chrome(driver_location)
    url = 'https://edu.ssafy.com/comm/login/SecurityLoginForm.do'
    driver.get(url)

    driver.find_element_by_name('userId').send_keys(user_id)
    driver.find_element_by_name('userPwd').send_keys(user_pwd)
    driver.find_element_by_xpath('//*[@id="wrap"]/div/div/div[4]/form/div/div[2]/div[3]/a').click()

    driver.get('https://edu.ssafy.com/edu/board/notice/list.do')

    driver.find_element_by_partial_link_text('중식').click()
    html = driver.page_source

    weekday = time.localtime().tm_wday

    soup = BeautifulSoup(html, 'html.parser')
    A = ''
    B = ''
    A_main = soup.select(f'#wrap > form > div > div.content > div > div:nth-child(1) > div.datail-content.mb20 > table > tbody > tr:nth-child(9) > td:nth-child({weekday + 4}) > p')[0].text
    B_main = soup.select(f'#wrap > form > div > div.content > div > div:nth-child(1) > div.datail-content.mb20 > table > tbody > tr:nth-child(17) > td:nth-child({weekday + 2}) > p')[0].text
    for i in range(10, 15):
        A += soup.select(f'#wrap > form > div > div.content > div > div:nth-child(1) > div.datail-content.mb20 > table > tbody > tr:nth-child({i}) > td:nth-child({weekday + 1}) > p')[0].text + ' '
        B += soup.select(f'#wrap > form > div > div.content > div > div:nth-child(1) > div.datail-content.mb20 > table > tbody > tr:nth-child({i + 8}) > td:nth-child({weekday + 1}) > p')[0].text + ' '
    drink = soup.select(f'#wrap > form > div > div.content > div > div:nth-child(1) > div.datail-content.mb20 > table > tbody > tr:nth-child(15) > td:nth-child({weekday + 1}) > p')[0].text

    result = f'오늘 중식의 A코스는 메인메뉴가 {A_main}이고 사이드메뉴는 {A}입니다.\n오늘 중식의 B코스는 메인메뉴가 {B_main}이고 사이드메뉴는 {B}입니다.\n음료수는 {drink}입니다.'
    # for test
    print(result)
    return result


def check_in_out_alarm(user_id, user_pwd, driver_location):
    driver = webdriver.Chrome(driver_location)
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
    # today= '2019-01-30'

    check_in_out = soup.select(f'a.fc-day-grid-event.fc-h-event.fc-event.fc-start.fc-end.cate.at01.event-on-{today}')
    early_check_out = soup.select(f'a.fc-day-grid-event.fc-h-event.fc-event.fc-start.fc-end.cate.at02.event-on-{today}')
    check = len(check_in_out)
    early = len(early_check_out)
    if check == 0:
        result = '아직 출석하지 않으셨습니다!'
    if check == 1:
        if early == 1:
            result = f'{early_check_out[0].text}'
        else:
            result = '아직 퇴실하지 않으셨습니다!'
    if check == 2:    
        if int(check_in_out[1].text[0:2]) < 18:
            result = '18시 이전에 퇴실 버튼을 누르셨습니다!'
        else:
            result = f'{check_in_out[0].text}\n{check_in_out[1].text}'
    # for test
    print(result)
    return result

# 11:50 마다 점심 메뉴 알려주기
schedule.every().day.at("11:50").do(lunch_menu, 'srs99125@naver.com', '##qQ036578', 'C:/Users/이상택/chromedriver.exe')
# 08:55 마다 출석 여부 알려주기
schedule.every().day.at("08:55").do(check_in_out_alarm, 'srs99125@naver.com', '##qQ036578', 'C:/Users/이상택/chromedriver.exe')
# 18:01 마다 퇴실 여부 알려주기
schedule.every().day.at("18:01").do(check_in_out_alarm, 'srs99125@naver.com', '##qQ036578', 'C:/Users/이상택/chromedriver.exe')

while 1:
    #스케줄 모듈을 계속해서 실행하기
    schedule.run_pending()
    time.sleep(1)