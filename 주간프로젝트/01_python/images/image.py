import urllib.request
import datetime
import requests
import csv

movies_name = []
movies_code = []

start_date = datetime.datetime(2019,1,13)
for i in range(10):
    t = start_date - datetime.timedelta(days=7 * i)
    target = t.strftime('%Y%m%d')
    
    key = 'e12be2ef03b4294b6b4ca0657423cbc6'
    URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={target}&weekGb=0'
    response = requests.get(URL).json()    
    response = response['boxOfficeResult']['weeklyBoxOfficeList']    

    for i in range(10):        
        movie_name = response[i]['movieNm']
        movies_name.append(movie_name)
        
movies_name = list(set(movies_name))

naver_uri = 'https://openapi.naver.com/v1/search/movie.json?query='

client_id = 'FaSdalhj1Twe1bDOc9uO'
client_secret = 'Fjx3tc_Alv'
headers = { 
    'X-Naver-Client-Id': client_id, 
    'X-Naver-Client-Secret': client_secret
}

for movie in movies_name:
    response = requests.get(naver_uri + movie, headers=headers).json()
    URL = response['items'][0]['image']
    name = f'{movie}' + '.jpg'
    urllib.request.urlretrieve(URL, name)
    #모든 파일의 확장자가 jpg인데 왜 몇몇 파일이 깨져서 나올까?



