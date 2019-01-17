import requests
from bs4 import BeautifulSoup

url = 'https://weather.naver.com/'

response = requests.get(url)
print(response.content)



# response = requests.get(url).txt
# soup = BeautifulSoup(response.content, 'html.parser')

# data_set = soup.select('.temp')
# area_l = ['서울/경기', '서해5도', '영서', '영동', '충북', '충남', '경북', '경남', '울릉도/독도', '전북', '전남', '제주도']
# for i in range(12):
#     print(f'{area_l[i]}의 현재 기온은 {data_set[i].text}입니다.')

