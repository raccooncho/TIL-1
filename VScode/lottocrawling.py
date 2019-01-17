import requests
from bs4 import BeautifulSoup

url = 'https://www.dhlottery.co.kr/common.do?method=main'

response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')
nums = []
lotto_nums = ""
for i in range(1, 7):
        nums = soup.select(f'#drwtNo{i}')
        lotto_nums += nums[0].text + ' '
bonus = soup.select('#bnusNo')
lotto_nums += '보너스 번호' + bonus[0].text
print(lotto_nums)
