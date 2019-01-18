import requests

URL = 'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837'
got = requests.get(URL)
print(got)
