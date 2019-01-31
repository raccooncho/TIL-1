import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/이상택/chromedriver.exe')

url = 'https://edu.ssafy.com/comm/login/SecurityLoginForm.do'
driver.get(url)

user_id = 'srs99125@naver.com'
user_pwd = '##qQ036578'
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

print(f'오늘 중식의 A코스는 메인메뉴가 {A_main}이고 사이드메뉴는  {A} 입니다.')
print(f'오늘 중식의 B코스는 메인메뉴가 {B_main}이고 사이드메뉴는  {B} 입니다.')
print(f'음료수는 {drink}입니다')