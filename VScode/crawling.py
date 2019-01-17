import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/'

response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

data_set = soup.select('.value')
data = data_set[2].text

print("JPY")
print(data)

