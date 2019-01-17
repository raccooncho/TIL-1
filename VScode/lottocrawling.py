import requests
from bs4 import BeautifulSoup

url = 'https://www.dhlottery.co.kr/common.do?method=main'

response = requests.get(url)
lotto_data = response.json()

lotto_nums = []

for k, v in lotto_data.items():
    if 'ball_645' in k:
        lotto_nums.append(v)

print(lotto_nums)
