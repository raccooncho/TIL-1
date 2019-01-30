import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/student/chromedriver.exe')
url = 'https://edu.ssafy.com/comm/login/SecurityLoginForm.do'
driver.get(url)

user_id = 'srs99125@naver.com'
user_pwd = '##qQ036578'
driver.find_element_by_name('userId').send_keys(user_id)
driver.find_element_by_name('userPwd').send_keys(user_pwd)
driver.find_element_by_xpath('//*[@id="wrap"]/div/div/div[4]/form/div/div[2]/div[3]/a').click()

driver.get('https://edu.ssafy.com/edu/board/notice/list.do')

driver.find_element_by_xpath('//*[@id="wrap"]/form/div/div[2]/div/div[1]/table[2]/tbody/tr[2]/td[2]/a').click()

html = driver.page_source
# url = 'https://edu.ssafy.com/edu/board/notice/detail.do'
# response = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
A = ''
B = ''
A_main = soup.select('#wrap > form > div > div.content > div > div:nth-child(1) > div.datail-content.mb20 > table > tbody > tr:nth-child(9) > td:nth-child(4) > p')[0].text
B_main = soup.select('#wrap > form > div > div.content > div > div:nth-child(1) > div.datail-content.mb20 > table > tbody > tr:nth-child(9) > td:nth-child(5) > p')[0].text
for i in range(10, 16):
    A += soup.select(f'#wrap > form > div > div.content > div > div:nth-child(1) > div.datail-content.mb20 > table > tbody > tr:nth-child({i}) > td:nth-child(1) > p')[0].text + ' '
    B += soup.select(f'#wrap > form > div > div.content > div > div:nth-child(1) > div.datail-content.mb20 > table > tbody > tr:nth-child({i}) > td:nth-child(2) > p')[0].text + ' '

print(f'오늘 중식의 A코스는 메인메뉴가 {A_main} 이고 사이드메뉴는  {A} 입니다.')
print(f'오늘 중식의 B코스는 메인메뉴가 {B_main} 이고 사이드메뉴는  {B} 입니다.')